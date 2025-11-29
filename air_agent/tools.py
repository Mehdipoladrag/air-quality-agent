import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")


# -------------------------------
# 1) GEOCODING
# -------------------------------
def geocode_city(city: str) -> dict:
    if not OPENWEATHER_KEY:
        return {"error": "Missing OPENWEATHER_KEY in .env", "lat": None, "lon": None}

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={OPENWEATHER_KEY}"
    data = requests.get(url).json()

    if not data:
        return {"error": f"City '{city}' not found.", "lat": None, "lon": None}

    return {
        "lat": data[0]["lat"],
        "lon": data[0]["lon"],
        "city": city,
    }


# -------------------------------
# 2) US AQI FORMULAS
# -------------------------------
def calc_us_aqi(concentration, breakpoints):
    for (Clow, Chigh, Ilow, Ihigh) in breakpoints:
        if Clow <= concentration <= Chigh:
            return ((Ihigh - Ilow) / (Chigh - Clow)) * (concentration - Clow) + Ilow
    return None


def calc_us_aqi_pm25(pm25):
    bp = [
        (0.0, 12.0, 0, 50),
        (12.1, 35.4, 51, 100),
        (35.5, 55.4, 101, 150),
        (55.5, 150.4, 151, 200),
        (150.5, 250.4, 201, 300),
        (250.5, 350.4, 301, 400),
        (350.5, 500.4, 401, 500),
    ]
    return calc_us_aqi(pm25, bp)


def calc_us_aqi_pm10(pm10):
    bp = [
        (0, 54, 0, 50),
        (55, 154, 51, 100),
        (155, 254, 101, 150),
        (255, 354, 151, 200),
        (355, 424, 201, 300),
        (425, 504, 301, 400),
        (505, 604, 401, 500),
    ]
    return calc_us_aqi(pm10, bp)


# -------------------------------
# 3) AIR QUALITY
# -------------------------------
def get_air_quality(lat: float, lon: float) -> dict:
    if not OPENWEATHER_KEY:
        return {"error": "Missing OPENWEATHER_KEY in .env"}

    url = (
        f"http://api.openweathermap.org/data/2.5/air_pollution?"
        f"lat={lat}&lon={lon}&appid={OPENWEATHER_KEY}"
    )

    data = requests.get(url).json()

    if "list" not in data or not data["list"]:
        return {"error": "Air quality data not available"}

    comp = data["list"][0]["components"]
    pm25 = comp["pm2_5"]
    pm10 = comp["pm10"]

    aqi_pm25 = calc_us_aqi_pm25(pm25)
    aqi_pm10 = calc_us_aqi_pm10(pm10)

    us_aqi = round(max(aqi_pm25, aqi_pm10))

    return {
        "us_aqi": us_aqi,
        "components": comp,
        "aqi_pm25": round(aqi_pm25),
        "aqi_pm10": round(aqi_pm10),
    }


# -------------------------------
# 4) WEATHER FORECAST
# -------------------------------
def get_weather_forecast(lat: float, lon: float) -> dict:
    if not OPENWEATHER_KEY:
        return {"error": "Missing OPENWEATHER_KEY in .env"}

    url = (
        f"http://api.openweathermap.org/data/2.5/forecast?"
        f"lat={lat}&lon={lon}&units=metric&appid={OPENWEATHER_KEY}"
    )

    data = requests.get(url).json()
    if "list" not in data:
        return {"error": "Weather forecast unavailable"}

    forecast = []

    for i in range(0, len(data["list"]), 8):
        day = data["list"][i]
        forecast.append({
            "date": day["dt_txt"],
            "temp": day["main"]["temp"],
            "weather": day["weather"][0]["description"],
        })

    return {"forecast": forecast}
