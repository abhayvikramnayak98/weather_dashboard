from dataclasses import dataclass
from typing import Optional
from utils.weather_conditions import (
    get_weather_description
)

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
    weather_description: str
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

    # --------------------------------
    # Hourly forecast
    # --------------------------------

    hourly_forecast: list["HourlyWeather"] | None = None

@dataclass
class HourlyWeather:

    # --------------------------------
    # Time
    # --------------------------------

    time: str

    # --------------------------------
    # Temperature
    # --------------------------------

    temperature: Optional[float] = None

    feels_like: Optional[float] = None

    # --------------------------------
    # Weather condition
    # --------------------------------

    weather_code: Optional[int] = None

    is_day: Optional[int] = None

    # --------------------------------
    # Precipitation
    # --------------------------------

    precipitation: Optional[float] = None

    rain: Optional[float] = None

    precipitation_probability: Optional[float] = None

    # --------------------------------
    # Wind
    # --------------------------------

    wind_speed: Optional[float] = None

    wind_direction: Optional[float] = None

    wind_gusts: Optional[float] = None

    # --------------------------------
    # UV
    # --------------------------------

    uv_index: Optional[float] = None

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
    # Hourly weather
    # --------------------------------

    hourly = (
        weather_response.get(
            "hourly",
            {}
        )
    )

    hourly_times = hourly.get(
        "time",
        []
    )

    hourly_temperatures = hourly.get(
        "temperature_2m",
        []
    )

    hourly_feels_like = hourly.get(
        "apparent_temperature",
        []
    )

    hourly_weather_codes = hourly.get(
        "weather_code",
        []
    )

    hourly_is_day = hourly.get(
        "is_day",
        []
    )

    hourly_precipitation = hourly.get(
        "precipitation",
        []
    )

    hourly_rain = hourly.get(
        "rain",
        []
    )

    hourly_precipitation_probability = (
        hourly.get(
            "precipitation_probability",
            []
        )
    )

    hourly_wind_speed = hourly.get(
        "wind_speed_10m",
        []
    )

    hourly_wind_direction = hourly.get(
        "wind_direction_10m",
        []
    )

    hourly_wind_gusts = hourly.get(
        "wind_gusts_10m",
        []
    )

    hourly_uv = hourly.get(
        "uv_index",
        []
    )

    # --------------------------------
    # Create hourly objects
    # --------------------------------

    hourly_forecast = []

    for index, time in enumerate(
        hourly_times
    ):

        hourly_forecast.append(
            HourlyWeather(

                time=time,

                temperature=(
                    hourly_temperatures[index]
                    if index < len(
                        hourly_temperatures
                    )
                    else None
                ),

                feels_like=(
                    hourly_feels_like[index]
                    if index < len(
                        hourly_feels_like
                    )
                    else None
                ),

                weather_code=(
                    hourly_weather_codes[index]
                    if index < len(
                        hourly_weather_codes
                    )
                    else None
                ),

                is_day=(
                    hourly_is_day[index]
                    if index < len(
                        hourly_is_day
                    )
                    else None
                ),

                precipitation=(
                    hourly_precipitation[index]
                    if index < len(
                        hourly_precipitation
                    )
                    else None
                ),

                rain=(
                    hourly_rain[index]
                    if index < len(
                        hourly_rain
                    )
                    else None
                ),

                precipitation_probability=(
                    hourly_precipitation_probability[
                        index
                    ]
                    if index < len(
                        hourly_precipitation_probability
                    )
                    else None
                ),

                wind_speed=(
                    hourly_wind_speed[index]
                    if index < len(
                        hourly_wind_speed
                    )
                    else None
                ),

                wind_direction=(
                    hourly_wind_direction[index]
                    if index < len(
                        hourly_wind_direction
                    )
                    else None
                ),

                wind_gusts=(
                    hourly_wind_gusts[index]
                    if index < len(
                        hourly_wind_gusts
                    )
                    else None
                ),

                uv_index=(
                    hourly_uv[index]
                    if index < len(
                        hourly_uv
                    )
                    else None
                ),
            )
        )

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
    # Weather condition
    # --------------------------------

    weather_code = current[
        "weather_code"
    ]

    weather_description = (
        get_weather_description(
            weather_code
        )
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
        weather_code=weather_code,

        weather_description=(
            weather_description
        ),

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
        
        # --------------------------------
        # Hourly forecast
        # --------------------------------

        hourly_forecast=hourly_forecast,
    )