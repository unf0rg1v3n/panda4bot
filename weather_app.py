import aiohttp
import asyncio
from datetime import datetime, timedelta

class OpenMeteoWeatherAsync:
    base_url = "https://api.open-meteo.com/v1/forecast"

    def __init__(self, latitude=54.9924, longitude=73.3686):
        self.params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "relative_humidity_2m", "weather_code", "wind_speed_10m"],
            "hourly": ["temperature_2m", "apparent_temperature", "precipitation_probability", "precipitation", "rain", "showers", "snowfall", "snow_depth", "weather_code", "visibility", "wind_gusts_10m"],
            "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "precipitation_hours"],
            "timezone": "auto",
            "forecast_days": 1
        }

    async def fetch_weather(self):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.base_url, params=self.params) as response:
                    data = await response.json()
                    return data
            except Exception as e:
                print(f"Error fetching weather data: {e}")
                return None

    @staticmethod
    def get_index(weather_code):
        associations = {
            0: "ясно☀️", 1: "преимущественно ясно🌤", 2: "переменная облачность⛅️", 3: "пасмурно☁️",
            45: "туман🌫", 48: "изморозь", 51: "мелкая морось🌦", 53: "моросящий дождь🌦",
            55: "моросящий дождь🌦", 56: "морось со льдом🌨", 57: "густая морось со льдом🌨",
            61: "слабый дождь🌧", 63: "дождь🌨. Время насладиться погодой☺️", 65: "дождь🌨",
            66: "дождь со льдом🌧", 67: "дождь со льдом🌧", 71: "слабый снегопад❄️", 73: "снег☃️",
            75: "сильный снегопад❄️", 77: "снегопад☃️", 80: "слабый ливневый дождь☔️",
            81: "ливень🌨", 82: "ливень🌨", 85: "сильный снегопад!☃️ Ура!", 86: "сильный снегопад!☃️ Ура!",
            95: "умеренная гроза🌩", 96: "гроза⛈", 97: "гроза⛈"
        }
        return associations.get(weather_code, "Неизвестный код погоды")

    @staticmethod
    def get_greeting():
        now = datetime.now() + timedelta(hours=1)
        if 4 < now.hour <= 12:
            return "🌅Доброе утро"
        elif 12 < now.hour <= 16:
            return "🏙Добрый день"
        elif 16 < now.hour <= 24:
            return "🌄Добрый вечер"
        else:
            return "🌌Доброй ночи"

    def update_params(self, new_params):
        self.params.update(new_params)


