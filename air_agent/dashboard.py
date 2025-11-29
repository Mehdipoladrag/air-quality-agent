import sys
import os
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from air_agent.tools import geocode_city, get_air_quality, get_weather_forecast


def build_report(city: str) -> str:
    geo = geocode_city(city)
    if "error" in geo or geo["lat"] is None:
        return f"❌ City not found: {city}"

    lat, lon = geo["lat"], geo["lon"]

    aq = get_air_quality(lat, lon)
    if "error" in aq:
        return f"❌ Air Quality Error: {aq['error']}"

    forecast = get_weather_forecast(lat, lon)

    aqi = aq["us_aqi"]
    comp = aq["components"]

    if aqi <= 50:
        cat = "Good 😊"
    elif aqi <= 100:
        cat = "Moderate 🙂"
    elif aqi <= 150:
        cat = "Unhealthy for Sensitive 😕"
    elif aqi <= 200:
        cat = "Unhealthy 😷"
    elif aqi <= 300:
        cat = "Very Unhealthy ☠️"
    else:
        cat = "Hazardous 💀"

    fcast = ""
    for day in forecast["forecast"]:
        fcast += f"- {day['date']}: {day['temp']}°C — {day['weather']}\n"

    return f"""
=== 🌫 AIR QUALITY REPORT ===
City: {city}
US AQI: {aqi}
Category: {cat}

Main Pollutants:
- PM2.5: {comp['pm2_5']} µg/m³
- PM10: {comp['pm10']} µg/m³
- O3: {comp['o3']}
- NO2: {comp['no2']}
- CO: {comp['co']}

=== 🌦 5-DAY WEATHER OUTLOOK ===
{fcast}
"""


def main():
    st.set_page_config(page_title="AI Air Assistant", page_icon="🌫", layout="wide")
    st.title("🤖🌫 AI Air Quality & Weather Assistant")

    city = st.text_input("City", "Tehran")

    if st.button("Ask AI"):
        with st.spinner("Loading..."):
            report = build_report(city)
        st.text(report)

    st.subheader("Visual Dashboard")

    city2 = st.text_input("City for dashboard", "Tehran", key="dash")

    if st.button("Show Dashboard"):
        with st.spinner("Loading..."):
            geo = geocode_city(city2)
            aq = get_air_quality(geo["lat"], geo["lon"])

        st.success("Data loaded!")
        aqi = aq["us_aqi"]
        comp = aq["components"]

        st.text(f"US AQI: {aqi}")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=aqi,
            gauge={"axis": {"range": [0, 500]}}
        ))
        st.plotly_chart(fig)

        df = pd.DataFrame({"Pollutant": list(comp.keys()), "Value": list(comp.values())})
        fig2 = px.bar(df, x="Pollutant", y="Value")
        st.plotly_chart(fig2)


if __name__ == "__main__":
    main()
