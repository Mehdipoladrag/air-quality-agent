from google.adk.agents.llm_agent import Agent
from .tools import geocode_city, get_air_quality, get_weather_forecast

root_agent = Agent(
    name="air_quality_agent",
    model="gemini-2.5-flash-lite",
    description="Gets air quality and weather forecast.",
    instruction=(
        "You MUST ALWAYS use the tools.\n"
        "1) geocode_city\n"
        "2) get_air_quality\n"
        "3) get_weather_forecast\n"
        "Provide formatted report.\n"
    ),
    tools=[geocode_city, get_air_quality, get_weather_forecast],
)

print("🌤️ Air Quality Agent Loaded!")
