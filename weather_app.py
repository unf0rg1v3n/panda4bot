from datetime import datetime, timedelta

import openmeteo_requests
import requests_cache
from retry_requests import retry


async def fetch_weather(latitude=54.9924, longitude=73.368):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "relative_humidity_2m", "weather_code", "wind_speed_10m"],
        "hourly": ["temperature_2m", "apparent_temperature", "precipitation_probability", "precipitation", "rain",
                   "showers", "snowfall", "snow_depth", "weather_code", "visibility", "wind_gusts_10m"],
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "precipitation_hours"],
        "timezone": "auto",
        "forecast_days": 1
    }
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)
    response = openmeteo.weather_api(base_url, params=params)[0]

    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_relative_humidity_2m = current.Variables(1).Value()

    daily = response.Daily()
    daily_weather_code = daily.Variables(0).ValuesAsNumpy()[0]
    daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()[0]
    daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()[0]

    return (f"{get_greeting()}\n"
            f"Сейчас в Омске {datetime.fromtimestamp(current.Time())}\n{int(current_temperature_2m)}°C, "
            f"{get_index(daily_weather_code)}\n"
            f"Влажность воздуха составляет {current_relative_humidity_2m}%\n"
            f"Максимальая температура сегодня составит {int(daily_temperature_2m_max)}°C, "
            f"минимальная {int(daily_temperature_2m_min)}°C")


def get_index(weather_code) -> str:
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


def get_greeting():
    now = datetime.now() + timedelta(hours=1)
    if 4 < now.hour <= 12:
        return "🌅Доброе утро!"
    elif 12 < now.hour <= 16:
        return "🏙Добрый день!"
    elif 16 < now.hour <= 24:
        return "🌄Добрый вечер!"
    else:
        return "🌌Доброй ночи!"
