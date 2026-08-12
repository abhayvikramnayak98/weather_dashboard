from tkinter import ttk

from ui.weather_sections import (
    CurrentConditionsSection,
    DailyForecastSection,
    WindSection,
    PrecipitationSection,
    AirQualitySection,
    SunUVSection,
)

from ui.hourly_forecast import HourlyForecastSection


class WeatherDashboard:

    def __init__(self, parent):

        self.parent = parent

        self.frame = ttk.Frame(
            parent
        )

        self.frame.pack(
            fill="x",
            padx=10,
            pady=8
        )

        # --------------------------------
        # Create sections
        # --------------------------------

        self.current_conditions = (
            CurrentConditionsSection(
                self.frame
            )
        )

        self.daily_forecast = (
            DailyForecastSection(
                self.frame
            )
        )

        self.wind = WindSection(
            self.frame
        )

        self.precipitation = (
            PrecipitationSection(
                self.frame
            )
        )

        self.air_quality = (
            AirQualitySection(
                self.frame
            )
        )

        self.sun_uv = SunUVSection(
            self.frame
        )

        # --------------------------------
        # Hourly forecast
        # --------------------------------

        self.hourly_forecast = (
            HourlyForecastSection(
                self.frame
            )
        )

        # --------------------------------
        # Responsive sections
        # --------------------------------

        self.sections = [
            self.current_conditions,
            self.daily_forecast,
            self.wind,
            self.precipitation,
            self.air_quality,
            self.sun_uv,
        ]

        # --------------------------------
        # Responsive resize
        # --------------------------------

        self.frame.bind(
            "<Configure>",
            self.on_resize
        )

    # --------------------------------
    # Responsive layout
    # --------------------------------

    def on_resize(
        self,
        event
    ):

        width = event.width

        if width <= 1:

            return

        if width >= 1000:

            layout = "wide"

        elif width >= 700:

            layout = "medium"

        else:

            layout = "narrow"

        self.apply_layout(
            layout,
            width
        )

    # --------------------------------
    # Apply layout
    # --------------------------------

    def apply_layout(
        self,
        layout,
        width
    ):

        # --------------------------------
        # Remove current section placement
        # --------------------------------

        for section in self.sections:

            section.frame.grid_forget()

        # --------------------------------
        # Hourly forecast placement
        # --------------------------------

        self.hourly_forecast.frame.grid_forget()

        # --------------------------------
        # Reset grid configuration
        # --------------------------------

        for column in range(3):

            self.frame.columnconfigure(
                column,
                weight=0,
                uniform=""
            )

        for row in range(8):

            self.frame.rowconfigure(
                row,
                weight=0
            )

        # ==============================================
        # Wide
        # ==============================================

        if layout == "wide":

            # --------------------------------
            # Two equal columns
            # --------------------------------

            self.frame.columnconfigure(
                0,
                weight=1,
                uniform="section"
            )

            self.frame.columnconfigure(
                1,
                weight=1,
                uniform="section"
            )

            # --------------------------------
            # Current Conditions
            # --------------------------------

            self.current_conditions.grid(
                0,
                0,
                columnspan=2
            )

            # --------------------------------
            # Daily Forecast
            # --------------------------------

            self.daily_forecast.grid(
                1,
                0,
                columnspan=2
            )

            # --------------------------------
            # Hourly Forecast
            # --------------------------------

            self.hourly_forecast.grid(
                2,
                0,
                columnspan=2
            )

            # --------------------------------
            # Wind / Precipitation
            # --------------------------------

            self.wind.grid(
                3,
                0
            )

            self.precipitation.grid(
                3,
                1
            )

            # --------------------------------
            # Air Quality / Sun & UV
            # --------------------------------

            self.air_quality.grid(
                4,
                0
            )

            self.sun_uv.grid(
                4,
                1
            )

        # ==============================================
        # Medium
        # ==============================================

        elif layout == "medium":

            # --------------------------------
            # Two equal columns
            # --------------------------------

            self.frame.columnconfigure(
                0,
                weight=1,
                uniform="section"
            )

            self.frame.columnconfigure(
                1,
                weight=1,
                uniform="section"
            )

            # --------------------------------
            # Current Conditions
            # --------------------------------

            self.current_conditions.grid(
                0,
                0,
                columnspan=2
            )

            # --------------------------------
            # Daily Forecast
            # --------------------------------

            self.daily_forecast.grid(
                1,
                0,
                columnspan=2
            )

            # --------------------------------
            # Hourly Forecast
            # --------------------------------

            self.hourly_forecast.grid(
                2,
                0,
                columnspan=2
            )

            # --------------------------------
            # Wind / Precipitation
            # --------------------------------

            self.wind.grid(
                3,
                0
            )

            self.precipitation.grid(
                3,
                1
            )

            # --------------------------------
            # Air Quality / Sun & UV
            # --------------------------------

            self.air_quality.grid(
                4,
                0
            )

            self.sun_uv.grid(
                4,
                1
            )

        # ==============================================
        # Narrow
        # ==============================================

        else:

            # --------------------------------
            # Single column
            # --------------------------------

            self.frame.columnconfigure(
                0,
                weight=1,
                uniform=""
            )

            # --------------------------------
            # Current Conditions
            # --------------------------------

            self.current_conditions.grid(
                0,
                0,
                columnspan=1
            )

            # --------------------------------
            # Daily Forecast
            # --------------------------------

            self.daily_forecast.grid(
                1,
                0,
                columnspan=1
            )

            # --------------------------------
            # Hourly Forecast
            # --------------------------------

            self.hourly_forecast.grid(
                2,
                0,
                columnspan=1
            )

            # --------------------------------
            # Wind
            # --------------------------------

            self.wind.grid(
                3,
                0,
                columnspan=1
            )

            # --------------------------------
            # Precipitation
            # --------------------------------

            self.precipitation.grid(
                4,
                0,
                columnspan=1
            )

            # --------------------------------
            # Air Quality
            # --------------------------------

            self.air_quality.grid(
                5,
                0,
                columnspan=1
            )

            # --------------------------------
            # Sun & UV
            # --------------------------------

            self.sun_uv.grid(
                6,
                0,
                columnspan=1
            )

        # --------------------------------
        # Update internal metric layouts
        # --------------------------------

        for section in self.sections:

            section.responsive_layout(
                width
            )

    # --------------------------------
    # Update weather
    # --------------------------------

    def update(
        self,
        weather,
        timezone_name=None
    ):

        self.current_conditions.update(
            weather
        )

        self.daily_forecast.update(
            weather.daily_forecast or []
        )

        self.wind.update(
            weather
        )

        self.precipitation.update(
            weather
        )

        self.air_quality.update(
            weather
        )

        self.sun_uv.update(
            weather
        )

        self.hourly_forecast.update(
            weather.hourly_forecast or [],
            timezone_name
        )

    # --------------------------------
    # Loading state
    # --------------------------------

    def update_loading(self):

        # --------------------------------
        # Existing weather sections
        # --------------------------------

        for section in self.sections:

            for metric in section.metrics:

                metric.set_value(
                    "Loading..."
                )

        # --------------------------------
        # Clear hourly forecast
        # --------------------------------

        self.hourly_forecast.update(
            []
        )