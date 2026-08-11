from tkinter import ttk

from ui.weather_sections import (
    CurrentConditionsSection,
    WindSection,
    PrecipitationSection,
    AirQualitySection,
    SunUVSection,
)


class WeatherDashboard:

    def __init__(self, parent):

        self.parent = parent

        self.frame = ttk.Frame(
            parent
        )

        self.frame.pack(
            fill="both",
            expand=True,
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

        self.sections = [
            self.current_conditions,
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
        # Reset grid configuration
        # --------------------------------

        for column in range(3):

            self.frame.columnconfigure(
                column,
                weight=0
            )

        for row in range(6):

            self.frame.rowconfigure(
                row,
                weight=0
            )

        # --------------------------------
        # Wide
        # --------------------------------

        if layout == "wide":

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

            self.current_conditions.grid(
                0,
                0,
                columnspan=2
            )

            self.wind.grid(
                1,
                0
            )

            self.precipitation.grid(
                1,
                1
            )

            self.air_quality.grid(
                2,
                0
            )

            self.sun_uv.grid(
                2,
                1
            )

        # --------------------------------
        # Medium
        # --------------------------------

        elif layout == "medium":

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

            self.current_conditions.grid(
                0,
                0,
                columnspan=2
            )

            self.wind.grid(
                1,
                0
            )

            self.precipitation.grid(
                1,
                1
            )

            self.air_quality.grid(
                2,
                0
            )

            self.sun_uv.grid(
                2,
                1
            )

        # --------------------------------
        # Narrow
        # --------------------------------

        else:

            self.frame.columnconfigure(
                0,
                weight=1
            )

            self.current_conditions.grid(
                0,
                0
            )

            self.wind.grid(
                1,
                0
            )

            self.precipitation.grid(
                2,
                0
            )

            self.air_quality.grid(
                3,
                0
            )

            self.sun_uv.grid(
                4,
                0
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
        weather
    ):

        self.current_conditions.update(
            weather
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

    # --------------------------------
    # Loading state
    # --------------------------------

    def update_loading(self):

        for section in self.sections:

            for metric in section.metrics:

                metric.set_value(
                    "Loading..."
                )