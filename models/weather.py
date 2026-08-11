from dataclasses import dataclass


@dataclass
class WeatherData:

    # --------------------------------
    # Temperature
    # --------------------------------

    temperature: float
    feels_like: float

    # --------------------------------
    # Atmospheric conditions
    # --------------------------------

    humidity: float
    dew_point: float
    cloud_cover: float

    # --------------------------------
    # Precipitation
    # --------------------------------

    precipitation: float
    rain: float

    # --------------------------------
    # Wind
    # --------------------------------

    wind_speed: float
    wind_direction: float
    wind_gusts: float

    # --------------------------------
    # Visibility / pressure
    # --------------------------------

    visibility: float
    surface_pressure: float

    # --------------------------------
    # Weather condition
    # --------------------------------

    weather_code: int
    is_day: int

    # --------------------------------
    # UV
    # --------------------------------

    uv_index: float

    # --------------------------------
    # Sun
    # --------------------------------

    sunrise: str | None = None
    sunset: str | None = None

    # --------------------------------
    # Air quality
    # --------------------------------

    aqi: float | None = None
    aqi_category: str | None = None

    pm25: float | None = None
    pm10: float | None = None

    ozone: float | None = None
    nitrogen_dioxide: float | None = None
    sulphur_dioxide: float | None = None
    carbon_monoxide: float | None = None

def get_aqi_category(aqi):

    if aqi is None:
        return None

    if aqi <= 50:
        return "Good"

    if aqi <= 100:
        return "Moderate"

    if aqi <= 150:
        return "Unhealthy for Sensitive Groups"

    if aqi <= 200:
        return "Unhealthy"

    if aqi <= 300:
        return "Very Unhealthy"

    return "Hazardous"

def create_weather_data(
    weather_response,
    air_quality_response
):

    current = weather_response["current"]

    # --------------------------------
    # Air quality
    # --------------------------------

    air_current = (
        air_quality_response.get(
            "current",
            {}
        )
    )

    aqi = air_current.get(
        "us_aqi"
    )

    # --------------------------------
    # Daily weather
    # --------------------------------

    daily = (
        weather_response.get(
            "daily",
            {}
        )
    )

    sunrise_values = (
        daily.get(
            "sunrise",
            []
        )
    )

    sunset_values = (
        daily.get(
            "sunset",
            []
        )
    )

    sunrise = (
        sunrise_values[0]
        if sunrise_values
        else None
    )

    sunset = (
        sunset_values[0]
        if sunset_values
        else None
    )

    # --------------------------------
    # Create WeatherData
    # --------------------------------

    return WeatherData(

        # Temperature
        temperature=current[
            "temperature_2m"
        ],

        feels_like=current[
            "apparent_temperature"
        ],

        # Atmospheric conditions
        humidity=current[
            "relative_humidity_2m"
        ],

        dew_point=current[
            "dew_point_2m"
        ],

        cloud_cover=current[
            "cloud_cover"
        ],

        # Precipitation
        precipitation=current[
            "precipitation"
        ],

        rain=current[
            "rain"
        ],

        # Wind
        wind_speed=current[
            "wind_speed_10m"
        ],

        wind_direction=current[
            "wind_direction_10m"
        ],

        wind_gusts=current[
            "wind_gusts_10m"
        ],

        # Visibility / pressure
        visibility=current[
            "visibility"
        ],

        surface_pressure=current[
            "surface_pressure"
        ],

        # Weather condition
        weather_code=current[
            "weather_code"
        ],

        is_day=current[
            "is_day"
        ],

        # UV
        uv_index=current[
            "uv_index"
        ],

        # Sun
        sunrise=sunrise,
        sunset=sunset,

        # Air quality
        aqi=aqi,

        aqi_category=get_aqi_category(
            aqi
        ),

        pm25=air_current.get(
            "pm2_5"
        ),

        pm10=air_current.get(
            "pm10"
        ),

        ozone=air_current.get(
            "ozone"
        ),

        nitrogen_dioxide=air_current.get(
            "nitrogen_dioxide"
        ),

        sulphur_dioxide=air_current.get(
            "sulphur_dioxide"
        ),

        carbon_monoxide=air_current.get(
            "carbon_monoxide"
        ),
    )