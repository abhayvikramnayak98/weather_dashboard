import tkinter as tk
from tkinter import ttk

from config.settings import (
    APP_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    MIN_WINDOW_WIDTH,
    MIN_WINDOW_HEIGHT,
    WEATHER_REFRESH_INTERVAL,
    FONT_TITLE,
    FONT_LOCATION,
    FONT_STATUS,
    FONT_FAMILY,
)

from services.weather_service import fetch_weather

from ui.clock import Clock
from ui.search_bar import SearchBar
from ui.weather_cards import WeatherCards


class MainWindow:

    def __init__(self, root):

        self.root = root

        self.root.title(APP_TITLE)

        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )

        self.root.minsize(
            MIN_WINDOW_WIDTH,
            MIN_WINDOW_HEIGHT
        )

        self.selected_location = None

        self.refresh_after_id = None

        self.request_generation = 0

        self.build_ui()

    # --------------------------------
    # Build UI
    # --------------------------------

    def build_ui(self):

        # --------------------------------
        # Header
        # --------------------------------

        header = ttk.Frame(
            self.root,
            padding=(20, 15)
        )

        header.pack(
            fill="x"
        )

        # Header columns
        header.columnconfigure(
            0,
            weight=1
        )

        header.columnconfigure(
            1,
            weight=1
        )

        # --------------------------------
        # Application title
        # --------------------------------

        self.title_label = ttk.Label(
            header,
            text="Weather Dashboard",
            font=FONT_TITLE,
            anchor="w"
        )

        self.title_label.grid(
            row=0,
            column=0,
            sticky="w"
        )

        # --------------------------------
        # Running clock
        # --------------------------------

        Clock(header)

        # --------------------------------
        # Responsive header
        # --------------------------------

        header.bind(
            "<Configure>",
            self.on_header_resize
        )

        # --------------------------------
        # City Search
        # --------------------------------

        SearchBar(
            self.root,
            self.location_selected
        )

        # --------------------------------
        # Selected Location
        # --------------------------------

        self.location_label = ttk.Label(
            self.root,
            text="No location selected",
            font=FONT_LOCATION
        )

        self.location_label.pack(
            anchor="w",
            padx=20,
            pady=(5, 0)
        )

        # --------------------------------
        # Status
        # --------------------------------

        self.status_label = ttk.Label(
            self.root,
            text="Search for a city to begin",
            font=FONT_STATUS
        )

        self.status_label.pack(
            anchor="w",
            padx=20,
            pady=(2, 5)
        )

        # --------------------------------
        # Weather Cards
        # --------------------------------

        self.weather_cards = WeatherCards(
            self.root
        )

    # --------------------------------
    # Responsive Header
    # --------------------------------

    def on_header_resize(self, event):

        width = event.width

        if width >= 1000:

            size = 24

        elif width >= 800:

            size = 20

        elif width >= 650:

            size = 17

        else:

            size = 14

        self.title_label.config(
            font=(
                FONT_FAMILY,
                size,
                "bold"
            )
        )

    # --------------------------------
    # Location Selected
    # --------------------------------

    def location_selected(self, location):

        self.selected_location = location

        # Invalidate previous requests.
        self.request_generation += 1

        generation = (
            self.request_generation
        )

        # Cancel scheduled refresh.
        self.cancel_refresh()

        # Display selected location.
        self.location_label.config(
            text=f"📍 {location.display_name}"
        )

        # Display loading state.
        self.status_label.config(
            text="Updating weather..."
        )

        self.weather_cards.update_loading()

        # Fetch weather in background.
        fetch_weather(
            location,
            lambda weather: self.weather_loaded(
                weather,
                generation
            ),
            lambda error: self.weather_error(
                error,
                generation
            )
        )

    # --------------------------------
    # Weather Loaded
    # --------------------------------

    def weather_loaded(
        self,
        weather,
        generation
    ):

        # Ignore stale responses.
        if generation != self.request_generation:

            return

        self.weather_cards.update(
            weather
        )

        print()
        print("========== WEATHER CONDITION ==========")

        print(
            "Code:",
            weather.weather_code
        )

        print(
            "Description:",
            weather.weather_description
        )

        print(
            "Day/Night:",
            "Day" if weather.is_day else "Night"
        )

        print("=======================================")

        print()
        print("========== AIR QUALITY ==========")

        print(
            "AQI:",
            weather.aqi
        )

        print(
            "AQI Category:",
            weather.aqi_category
        )

        print(
            "PM2.5:",
            weather.pm25
        )

        print(
            "PM10:",
            weather.pm10
        )

        print(
            "Ozone:",
            weather.ozone
        )

        print(
            "NO2:",
            weather.nitrogen_dioxide
        )

        print(
            "SO2:",
            weather.sulphur_dioxide
        )

        print(
            "CO:",
            weather.carbon_monoxide
        )

        print(
            "================================="
        )

        self.status_label.config(
            text="Updated just now"
        )

        print("Temperature:", weather.temperature)
        print("Feels like:", weather.feels_like)
        print("Dew point:", weather.dew_point)
        print("Cloud cover:", weather.cloud_cover)
        print("Precipitation:", weather.precipitation)
        print("Rain:", weather.rain)
        print("Wind gusts:", weather.wind_gusts)
        print("Pressure:", weather.surface_pressure)
        print("UV:", weather.uv_index)
        print("Day:", weather.is_day)
        print("Sunrise:", weather.sunrise)
        print("Sunset:", weather.sunset)

        self.schedule_refresh()

    # --------------------------------
    # Weather Error
    # --------------------------------

    def weather_error(
        self,
        error,
        generation
    ):

        # Ignore stale responses.
        if generation != self.request_generation:

            return

        print(
            f"Weather error: {error}"
        )

        self.status_label.config(
            text="Unable to update weather"
        )

        self.schedule_refresh()

    # --------------------------------
    # Automatic Refresh
    # --------------------------------

    def schedule_refresh(self):

        self.cancel_refresh()

        if self.selected_location is None:

            return

        self.refresh_after_id = (
            self.root.after(
                WEATHER_REFRESH_INTERVAL,
                self.refresh_weather
            )
        )

    def refresh_weather(self):

        if self.selected_location is None:

            return

        self.request_generation += 1

        generation = (
            self.request_generation
        )

        self.status_label.config(
            text="Updating weather..."
        )

        self.weather_cards.update_loading()

        fetch_weather(
            self.selected_location,
            lambda weather: self.weather_loaded(
                weather,
                generation
            ),
            lambda error: self.weather_error(
                error,
                generation
            )
        )

    # --------------------------------
    # Cancel Refresh
    # --------------------------------

    def cancel_refresh(self):

        if self.refresh_after_id is not None:

            self.root.after_cancel(
                self.refresh_after_id
            )

            self.refresh_after_id = None