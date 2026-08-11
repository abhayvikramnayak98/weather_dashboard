import requests

from config.settings import WEATHER_URL


def get_current_weather(
    latitude: float,
    longitude: float,
    timezone: str = "auto",
):

    response = requests.get(
        WEATHER_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": (
    "temperature_2m,"
    "apparent_temperature,"
    "relative_humidity_2m,"
    "wind_speed_10m,"
    "wind_direction_10m,"
    "visibility,"
    "weather_code"
),
            "timezone": timezone,
        },
        timeout=10,
    )

    response.raise_for_status()

    return response.json()