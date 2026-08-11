from dataclasses import dataclass


@dataclass
class WeatherData:

    temperature: float
    feels_like: float

    humidity: float

    wind_speed: float
    wind_direction: float

    visibility: float

    weather_code: int

    aqi: float | None = None
    pm25: float | None = None


def create_weather_data(
    weather_response,
    air_quality_response
):

    current = weather_response["current"]

    air_current = (
        air_quality_response.get(
            "current",
            {}
        )
    )

    return WeatherData(

    temperature=current[
        "temperature_2m"
    ],

    feels_like=current[
        "apparent_temperature"
    ],

    humidity=current[
        "relative_humidity_2m"
    ],

    wind_speed=current[
        "wind_speed_10m"
    ],

    wind_direction=current[
        "wind_direction_10m"
    ],

    visibility=current[
        "visibility"
    ],

    weather_code=current[
        "weather_code"
    ],

    aqi=air_current.get(
        "us_aqi"
    ),

    pm25=air_current.get(
        "pm2_5"
    ),
)