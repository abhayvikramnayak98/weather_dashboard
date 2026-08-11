import threading

from api.weather import get_current_weather
from api.air_quality import get_current_air_quality

from models.location import Location
from models.weather import create_weather_data


def fetch_weather(
    location: Location,
    on_success,
    on_error,
):

    def worker():

        try:

            weather_response = (
                get_current_weather(
                    latitude=location.latitude,
                    longitude=location.longitude,
                    timezone=location.timezone,
                )
            )

            air_quality_response = (
                get_current_air_quality(
                    latitude=location.latitude,
                    longitude=location.longitude,
                    timezone=location.timezone,
                )
            )

            weather_data = (
                create_weather_data(
                    weather_response,
                    air_quality_response
                )
            )

            on_success(
                weather_data
            )

        except Exception as error:

            on_error(error)

    thread = threading.Thread(
        target=worker,
        daemon=True
    )

    thread.start()