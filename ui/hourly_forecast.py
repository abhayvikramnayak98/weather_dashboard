from datetime import datetime

import tkinter as tk
from tkinter import ttk

from config.settings import FONT_FAMILY


# ==============================================
# Hourly Forecast Card
# ==============================================

class HourlyForecastCard:

    def __init__(
        self,
        parent
    ):

        self.frame = ttk.Frame(
            parent,
            padding=(12, 8)
        )

        # --------------------------------
        # Time
        # --------------------------------

        self.time_label = ttk.Label(
            self.frame,
            text="—",
            font=(
                FONT_FAMILY,
                9,
                "bold"
            ),
            anchor="center"
        )

        self.time_label.pack(
            fill="x"
        )

        # --------------------------------
        # Weather condition
        # --------------------------------

        self.condition_label = ttk.Label(
            self.frame,
            text="—",
            font=(
                FONT_FAMILY,
                18
            ),
            anchor="center",
            justify="center"
        )

        self.condition_label.pack(
            fill="x",
            pady=(5, 3)
        )

        # --------------------------------
        # Temperature
        # --------------------------------

        self.temperature_label = ttk.Label(
            self.frame,
            text="—",
            font=(
                FONT_FAMILY,
                13,
                "bold"
            ),
            anchor="center"
        )

        self.temperature_label.pack(
            fill="x"
        )

        # --------------------------------
        # Feels like
        # --------------------------------

        self.feels_like_label = ttk.Label(
            self.frame,
            text="Feels like —",
            font=(
                FONT_FAMILY,
                8
            ),
            anchor="center"
        )

        self.feels_like_label.pack(
            fill="x",
            pady=(3, 6)
        )

        # --------------------------------
        # Precipitation probability
        # --------------------------------

        self.precipitation_label = ttk.Label(
            self.frame,
            text="Precip —",
            font=(
                FONT_FAMILY,
                8
            ),
            anchor="center"
        )

        self.precipitation_label.pack(
            fill="x"
        )

        # --------------------------------
        # Wind
        # --------------------------------

        self.wind_label = ttk.Label(
            self.frame,
            text="Wind —",
            font=(
                FONT_FAMILY,
                8
            ),
            anchor="center"
        )

        self.wind_label.pack(
            fill="x",
            pady=(3, 0)
        )

    # --------------------------------
    # Update card
    # --------------------------------

    def update(
        self,
        hour
    ):

        # --------------------------------
        # Time / current hour
        # --------------------------------

        time_text = hour.time

        try:

            forecast_time = datetime.fromisoformat(
                time_text
            )

            current_time = datetime.now()

            is_current_hour = (
                forecast_time.year
                == current_time.year
                and
                forecast_time.month
                == current_time.month
                and
                forecast_time.day
                == current_time.day
                and
                forecast_time.hour
                == current_time.hour
            )

        except (
            ValueError,
            TypeError
        ):

            is_current_hour = False

        # --------------------------------
        # Display time
        # --------------------------------

        if is_current_hour:

            time_text = "NOW"

        else:

            time_text = self.format_time(
                hour.time
            )

        self.time_label.config(
            text=time_text
        )

        # Weather condition
        self.condition_label.config(
            text=self.get_weather_symbol(
                hour.weather_code,
                hour.is_day
            )
        )

        # Temperature
        if hour.temperature is not None:

            self.temperature_label.config(
                text=f"{hour.temperature:.1f} °C"
            )

        else:

            self.temperature_label.config(
                text="—"
            )

        # Feels like
        if hour.feels_like is not None:

            self.feels_like_label.config(
                text=(
                    f"Feels like "
                    f"{hour.feels_like:.1f} °C"
                )
            )

        else:

            self.feels_like_label.config(
                text="Feels like —"
            )

        # Precipitation probability
        if (
            hour.precipitation_probability
            is not None
        ):

            self.precipitation_label.config(
                text=(
                    "Precip "
                    f"{hour.precipitation_probability:.0f}%"
                )
            )

        else:

            self.precipitation_label.config(
                text="Precip —"
            )

        # Wind
        if hour.wind_speed is not None:

            wind_text = (
                f"Wind "
                f"{hour.wind_speed:.1f} km/h"
            )

            self.wind_label.config(
                text=wind_text
            )

        else:

            self.wind_label.config(
                text="Wind —"
            )

    # --------------------------------
    # Format forecast time
    # --------------------------------

    @staticmethod
    def format_time(
        time_text
    ):

        try:

            if "T" in time_text:

                time_text = time_text.split(
                    "T",
                    1
                )[1]

            hour = int(
                time_text[:2]
            )

            if hour == 0:

                return "12 AM"

            if hour < 12:

                return f"{hour} AM"

            if hour == 12:

                return "12 PM"

            return f"{hour - 12} PM"

        except (
            ValueError,
            TypeError,
            IndexError
        ):

            return time_text

    # --------------------------------
    # Weather symbol
    # --------------------------------

    @staticmethod
    def get_weather_symbol(
        weather_code,
        is_day
    ):

        if weather_code is None:

            return "—"

        if weather_code == 0:

            return "☀️" if is_day else "🌙"

        if weather_code in (
            1,
            2
        ):

            return "🌤️" if is_day else "☁️"

        if weather_code == 3:

            return "☁️"

        if weather_code in (
            45,
            48
        ):

            return "🌫️"

        if weather_code in (
            51,
            53,
            55,
            56,
            57
        ):

            return "🌦️"

        if weather_code in (
            61,
            63,
            65,
            66,
            67
        ):

            return "🌧️"

        if weather_code in (
            71,
            73,
            75,
            77
        ):

            return "❄️"

        if weather_code in (
            80,
            81,
            82
        ):

            return "🌧️"

        if weather_code in (
            95,
            96,
            99
        ):

            return "⛈️"

        return "🌡️"

    # --------------------------------
    # Grid
    # --------------------------------

    def grid(
        self,
        row,
        column
    ):

        self.frame.grid(
            row=row,
            column=column,
            padx=4,
            pady=4,
            sticky="nsew"
        )


# ==============================================
# Hourly Forecast Section
# ==============================================

class HourlyForecastSection:

    def __init__(
        self,
        parent
    ):

        self.frame = ttk.Frame(
            parent,
            style="WeatherCard.TFrame",
            padding=(18, 16)
        )

        # --------------------------------
        # Section title
        # --------------------------------

        self.title_label = ttk.Label(
            self.frame,
            text="HOURLY FORECAST",
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
            pady=(0, 14)
        )

        # --------------------------------
        # Horizontal canvas
        # --------------------------------

        self.canvas = tk.Canvas(
            self.frame,
            height=170,
            highlightthickness=0,
            borderwidth=0
        )

        self.canvas.pack(
            fill="x",
            expand=True
        )

        # --------------------------------
        # Horizontal scrollbar
        # --------------------------------

        self.scrollbar = ttk.Scrollbar(
            self.frame,
            orient="horizontal",
            command=self.canvas.xview
        )

        self.scrollbar.pack(
            fill="x",
            pady=(4, 0)
        )

        self.canvas.configure(
            xscrollcommand=self.scrollbar.set
        )

        # --------------------------------
        # Scrollable cards frame
        # --------------------------------

        self.content = ttk.Frame(
            self.canvas
        )

        self.window_id = (
            self.canvas.create_window(
                (0, 0),
                window=self.content,
                anchor="nw"
            )
        )

        self.content.bind(
            "<Configure>",
            self.on_content_configure
        )

        self.canvas.bind(
            "<Configure>",
            self.on_canvas_configure
        )

        self.cards = []

    # --------------------------------
    # Content resize
    # --------------------------------

    def on_content_configure(
        self,
        event
    ):

        self.canvas.configure(
            scrollregion=self.canvas.bbox(
                "all"
            )
        )

    # --------------------------------
    # Canvas resize
    # --------------------------------

    def on_canvas_configure(
        self,
        event
    ):

        self.canvas.itemconfigure(
            self.window_id,
            height=event.height
        )

    # --------------------------------
    # Update forecast
    # --------------------------------

    def update(
        self,
        hourly_forecast
    ):

        for card in self.cards:

            card.frame.destroy()

        self.cards.clear()

        for hour in hourly_forecast:

            card = HourlyForecastCard(
                self.content
            )

            card.update(
                hour
            )

            card.grid(
                0,
                len(self.cards)
            )

            self.cards.append(
                card
            )

        self.content.update_idletasks()

        self.canvas.configure(
            scrollregion=self.canvas.bbox(
                "all"
            )
        )

    # --------------------------------
    # Grid placement
    # --------------------------------

    def grid(
        self,
        row,
        column,
        columnspan=1
    ):

        self.frame.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=8,
            pady=8,
            sticky="nsew"
        )