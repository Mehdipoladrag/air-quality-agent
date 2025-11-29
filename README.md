# 🌍 **air-quality-agent**

A smart, lightweight agent for retrieving **air quality data**, **weather forecasts**, and **city geocoding** using external APIs.  
Includes an interactive **Streamlit dashboard** for real-time exploration.


---

<!-- Badges / Logos -->
<p align="center">
  <img alt="VSCode" src="https://img.shields.io/badge/VSCode-Visual%20Studio%20Code-blue?logo=visual-studio-code" />&nbsp;
  <img alt="Gemini" src="https://img.shields.io/badge/Gemini-Google%20Gemini-4285F4?logo=google" />&nbsp;
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />&nbsp;
  <img alt="AI Agent" src="https://img.shields.io/badge/AI-Agent-Assistant-orange?logo=robot" />&nbsp;
  <img alt="Kaggle" src="https://img.shields.io/badge/Kaggle-mehdip1-20BEFF?logo=kaggle" />
</p>

## ✨ Features

- 🔍 **City geocoding** via the Open-Meteo API  
- 🌫️ **Air Quality Index (AQI)** retrieval  
- 🌦️ **Multi-day weather forecast**  
- 🤖 **Simple intelligent Agent module** for natural-language queries  
- 📊 **Streamlit dashboard** for visual interaction and quick testing  

---

## 📁 Project Structure

```
air_quality_agent/
│
├── air_agent/
│   ├── __init__.py
│   ├── tools.py
│   ├── agent.py
│   ├── dashboard.py
│   └── test.py
│
└── README.md
```

---
## 🔑 Getting API Keys

To run this project, you must obtain two API keys:

---

### 1️⃣ **OpenWeatherMap API Key**

1. Go to: https://openweathermap.org/city/112931  
2. Sign up or log in to your account.  
3. Navigate to:  
   **Dashboard → API Keys**  
4. Create a new key and copy it.

Add it to your `.env` file as:

```
OPENWEATHER_KEY=YOUR_OPENWEATHER_KEY_HERE
```

---

### 2️⃣ **Google AI Studio (Gemini) API Key**

1. Visit: https://aistudio.google.com/api-keys  
2. Click **“Create API Key”**  
3. Select a project or create a new one  
4. Copy your API key  

Add it to your `.env` file:

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

---

## ✅ Your `.env` file should look like:

```
OPENWEATHER_KEY=xxxxxxxxxxxxxxxxxxxx
GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxx
```

Make sure the `.env` file is placed in the project root.

---
## ▶️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/air-quality-agent.git
cd air-quality-agent
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

Minimal requirements file:

```
requests
streamlit
```

---

## 🚀 Run the Dashboard

```bash
streamlit run air_agent/dashboard.py
```

---

## 🧠 Using the Agent (programmatically)

```python
from air_agent.agent import AirAgent

agent = AirAgent()

response = agent.ask("What is the air quality in Berlin?")
print(response)
```

---

## 🛠️ API Notes

This project uses the free APIs from **Open-Meteo**:

- Geocoding: https://open-meteo.com/en/docs/geocoding-api  
- Air Quality: https://open-meteo.com/en/docs/air-quality-api  
- Weather Forecast: https://open-meteo.com/en/docs  

No API keys required.

---

## 🤝 Contributing

Pull requests are welcome!  
Please open an issue first to discuss major changes.

---

## 📄 License

MIT License.  
Feel free to use, modify, and distribute.

## 📬 Contact

Feel free to reach out or follow my work:

- **GitHub:** https://github.com/Mehdipoladrag
- **Kaggle:** https://www.kaggle.com/mehdip1  
- **Email:** mehdipoladrag1382@gmail.com

<p>
  <a href="https://github.com/Mehdipoladrag">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-yourusername-181717?logo=github" />
  </a>
  &nbsp;
  <a href="https://www.kaggle.com/mehdip1">
    <img alt="Kaggle" src="https://img.shields.io/badge/Kaggle-mehdip1-20BEFF?logo=kaggle" />
  </a>
  &nbsp;
  <a href="mehdipoladrag1382@gmail.com">
    <img alt="Email" src="https://img.shields.io/badge/Email-Contact-orange?logo=gmail" />
  </a>
</p>
