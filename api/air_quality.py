import requests

from config.settings import AIR_QUALITY_URL


def get_current_air_quality(
    latitude: float,
    longitude: float,
    timezone: str = "auto",
):

    response = requests.get(
        AIR_QUALITY_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "us_aqi,"
                "pm2_5"
            ),
            "timezone": timezone,
        },
        timeout=10,
    )

    response.raise_for_status()

    return response.json()