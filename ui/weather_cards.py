from tkinter import ttk

from config.settings import (
    FONT_METRIC,
    FONT_SMALL,
    FONT_FAMILY,
)

from utils.compass import degrees_to_compass


class MetricCard:

    def __init__(
        self,
        parent,
        title,
    ):

        self.frame = ttk.Frame(
            parent,
            style="WeatherCard.TFrame",
            padding=(20, 16)
        )

        # --------------------------------
        # Card title
        # --------------------------------

        self.title_label = ttk.Label(
            self.frame,
            text=title.upper(),
            font=(
                FONT_FAMILY,
                10,
                "bold"
            ),
            style="WeatherCardTitle.TLabel",
            anchor="w"
        )

        self.title_label.pack(
            fill="x",
            pady=(0, 12)
        )

        # --------------------------------
        # Main value
        # --------------------------------

        self.value_label = ttk.Label(
            self.frame,
            text="—",
            font=FONT_METRIC,
            style="WeatherMetric.TLabel",
            anchor="center"
        )

        self.value_label.pack(
            fill="both",
            expand=True,
            pady=(5, 3)
        )

        # --------------------------------
        # Secondary value
        # --------------------------------

        self.subtitle_label = ttk.Label(
            self.frame,
            text="",
            font=FONT_SMALL,
            style="WeatherSecondary.TLabel",
            anchor="center"
        )

        self.subtitle_label.pack(
            fill="x",
            pady=(3, 4)
        )

    # --------------------------------
    # Grid placement
    # --------------------------------

    def grid(
        self,
        row,
        column
    ):

        self.frame.grid(
            row=row,
            column=column,
            padx=6,
            pady=6,
            sticky="nsew"
        )

    # --------------------------------
    # Update card
    # --------------------------------

    def update(
        self,
        value,
        subtitle=""
    ):

        self.value_label.config(
            text=value
        )

        self.subtitle_label.config(
            text=subtitle
        )


class WeatherCards:

    def __init__(self, parent):

        self.parent = parent

        self.frame = ttk.Frame(
            parent
        )

        self.frame.pack(
            fill="both",
            expand=True,
            padx=16,
            pady=8
        )

        self.create_cards()

        self.current_columns = 2

        self.frame.bind(
            "<Configure>",
            self.on_resize
        )

        self.update_grid()

    # --------------------------------
    # Create cards
    # --------------------------------

    def create_cards(self):

        self.temperature_card = MetricCard(
            self.frame,
            "Temperature"
        )

        self.wind_card = MetricCard(
            self.frame,
            "Wind Speed"
        )

        self.direction_card = MetricCard(
            self.frame,
            "Wind Direction"
        )

        self.humidity_card = MetricCard(
            self.frame,
            "Humidity"
        )

        self.visibility_card = MetricCard(
            self.frame,
            "Visibility"
        )

        self.aqi_card = MetricCard(
            self.frame,
            "Air Quality"
        )

        self.cards = [
            self.temperature_card,
            self.wind_card,
            self.direction_card,
            self.humidity_card,
            self.visibility_card,
            self.aqi_card,
        ]

    # --------------------------------
    # Responsive layout
    # --------------------------------

    def on_resize(self, event):

        width = event.width

        if width < 650:

            columns = 1

        else:

            columns = 2

        if columns != self.current_columns:

            self.current_columns = columns

            self.update_grid()

    # --------------------------------
    # Update grid
    # --------------------------------

    def update_grid(self):

        for card in self.cards:

            card.frame.grid_forget()

        # Reset columns
        for column in range(2):

            self.frame.columnconfigure(
                column,
                weight=0
            )

        # Active columns
        for column in range(
            self.current_columns
        ):

            self.frame.columnconfigure(
                column,
                weight=1,
                uniform="weather_card"
            )

        # Reset rows
        for row in range(6):

            self.frame.rowconfigure(
                row,
                weight=0
            )

        # 2-column layout
        if self.current_columns == 2:

            for row in range(3):

                self.frame.rowconfigure(
                    row,
                    weight=1
                )

        # 1-column layout
        else:

            for row in range(6):

                self.frame.rowconfigure(
                    row,
                    weight=1
                )

        # Place cards
        for index, card in enumerate(
            self.cards
        ):

            row = (
                index // self.current_columns
            )

            column = (
                index % self.current_columns
            )

            card.grid(
                row,
                column
            )

    # --------------------------------
    # Loading
    # --------------------------------

    def update_loading(self):

        self.temperature_card.update(
            "Loading..."
        )

        self.wind_card.update(
            "Loading..."
        )

        self.direction_card.update(
            "Loading..."
        )

        self.humidity_card.update(
            "Loading..."
        )

        self.visibility_card.update(
            "Loading..."
        )

        self.aqi_card.update(
            "Loading..."
        )

    # --------------------------------
    # Weather data
    # --------------------------------

    def update(self, weather):

        # Temperature
        self.temperature_card.update(
            f"{weather.temperature:.1f} °C",
            f"Feels like {weather.feels_like:.1f} °C"
        )

        # Wind speed
        self.wind_card.update(
            f"{weather.wind_speed:.1f} km/h"
        )

        # Wind direction
        direction = degrees_to_compass(
            weather.wind_direction
        )

        self.direction_card.update(
            f"{weather.wind_direction:.0f}° {direction}"
        )

        # Humidity
        self.humidity_card.update(
            f"{weather.humidity:.0f}%"
        )

        # Visibility
        visibility_km = (
            weather.visibility / 1000
        )

        self.visibility_card.update(
            f"{visibility_km:.1f} km"
        )

        # AQI
        if weather.aqi is not None:

            aqi_value = (
                f"AQI {weather.aqi:.0f}"
            )

        else:

            aqi_value = "AQI —"

        # PM2.5
        if weather.pm25 is not None:

            pm25_value = (
                f"PM2.5 {weather.pm25:.1f} μg/m³"
            )

        else:

            pm25_value = "PM2.5 —"

        self.aqi_card.update(
            aqi_value,
            pm25_value
        )