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

            # --------------------------------
            # Current weather variables
            # --------------------------------

            "current": (
                "temperature_2m,"
                "apparent_temperature,"
                "relative_humidity_2m,"
                "wind_speed_10m,"
                "wind_direction_10m,"
                "wind_gusts_10m,"
                "visibility,"
                "weather_code,"
                "dew_point_2m,"
                "cloud_cover,"
                "precipitation,"
                "rain,"
                "surface_pressure,"
                "uv_index,"
                "is_day"
            ),

            # --------------------------------
            # Hourly weather variables
            # --------------------------------

            "hourly": (
                "temperature_2m,"
                "apparent_temperature,"
                "weather_code,"
                "is_day,"
                "precipitation,"
                "rain,"
                "precipitation_probability,"
                "wind_speed_10m,"
                "wind_direction_10m,"
                "wind_gusts_10m,"
                "uv_index"
            ),

            # --------------------------------
            # Daily variables
            # --------------------------------

            "daily": (
                "sunrise,"
                "sunset"
            ),

            # --------------------------------
            # Location timezone
            # --------------------------------

            "timezone": timezone,

            # We only need today's sunrise/sunset.
            "forecast_days": 2,
        },

        timeout=10,
    )

    response.raise_for_status()

    return response.json()