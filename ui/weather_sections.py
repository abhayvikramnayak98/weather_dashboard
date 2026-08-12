from tkinter import Canvas, ttk

from config.settings import FONT_FAMILY
from utils.compass import degrees_to_compass


# ==============================================
# Base Weather Section
# ==============================================

class WeatherSection:

    def __init__(
        self,
        parent,
        title,
    ):

        self.parent = parent

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
            pady=(0, 14)
        )

        # --------------------------------
        # Content area
        # --------------------------------

        self.content = ttk.Frame(
            self.frame
        )

        self.content.pack(
            fill="both",
            expand=True
        )

        self.metrics = []

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
            padx=6,
            pady=6,
            sticky="nsew"
        )

    # --------------------------------
    # Clear content
    # --------------------------------

    def clear(self):

        for widget in self.content.winfo_children():

            widget.destroy()

    # --------------------------------
    # Layout metrics
    # --------------------------------

    def layout_metrics(
        self,
        columns
    ):

        for metric in self.metrics:

            metric.frame.grid_forget()

        # --------------------------------
        # Reset columns
        # --------------------------------

        for column in range(8):

            self.content.columnconfigure(
                column,
                weight=0,
                uniform=""
            )

        # --------------------------------
        # Configure active columns
        # --------------------------------

        for column in range(columns):

            self.content.columnconfigure(
                column,
                weight=1,
                uniform="metric"
            )

        # --------------------------------
        # Reset rows
        # --------------------------------

        for row in range(8):

            self.content.rowconfigure(
                row,
                weight=0
            )

        # --------------------------------
        # Configure active rows
        # --------------------------------

        row_count = (
            len(self.metrics) + columns - 1
        ) // columns

        for row in range(row_count):

            self.content.rowconfigure(
                row,
                weight=1
            )

    # --------------------------------
    # Place metrics
    # --------------------------------

        for index, metric in enumerate(
            self.metrics
        ):

            row = index // columns
            column = index % columns

            metric.grid(
                row,
                column
            )

    # --------------------------------
    # Responsive layout
    # --------------------------------

    def responsive_layout(
        self,
        width
    ):

        if width >= 900:

            columns = 4

        elif width >= 600:

            columns = 2

        else:

            columns = 1

        self.layout_metrics(
            columns
        )


# ==============================================
# Weather Metric
# ==============================================

class WeatherMetric:

    def __init__(
        self,
        parent,
        label,
        value="—",
    ):

        self.frame = ttk.Frame(
            parent
        )

        # --------------------------------
        # Metric label
        # --------------------------------

        self.label = ttk.Label(
            self.frame,
            text=label.upper(),
            font=(
                FONT_FAMILY,
                8,
                "bold"
            ),
            style="WeatherSecondary.TLabel",
            anchor="w"
        )

        self.label.pack(
            fill="x"
        )

        # --------------------------------
        # Metric value
        # --------------------------------

        self.value = ttk.Label(
            self.frame,
            text=value,
            font=(
                FONT_FAMILY,
                12,
                "bold"
            ),
            style="WeatherMetric.TLabel",
            anchor="w",
            justify="left",
            wraplength=1
        )

        self.value.pack(
            fill="x",
            pady=(3, 0)
        )

        # --------------------------------
        # Responsive value wrapping
        # --------------------------------

        self.frame.bind(
            "<Configure>",
            self.on_resize
        )

    # --------------------------------
    # Responsive value layout
    # --------------------------------

    def on_resize(
        self,
        event
    ):

        width = event.width

        wrap_width = max(
            width - 16,
            1
        )

        self.value.configure(
            wraplength=wrap_width
        )

    # --------------------------------
    # Update value
    # --------------------------------

    def set_value(
        self,
        value
    ):

        self.value.config(
            text=value
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
            padx=8,
            pady=6,
            sticky="nsew"
        )

# ==============================================
# Daily Forecast Card
# ==============================================

class DailyForecastCard:

    def __init__(
        self,
        parent
    ):

        self.frame = ttk.Frame(
            parent,
            style="WeatherCard.TFrame",
            padding=(12, 12)
        )

        # --------------------------------
        # Day
        # --------------------------------

        self.day = ttk.Label(
            self.frame,
            text="—",
            font=(
                FONT_FAMILY,
                9,
                "bold"
            ),
            style="WeatherCardTitle.TLabel",
            anchor="center"
        )

        self.day.pack(
            fill="x"
        )

        # --------------------------------
        # Weather symbol
        # --------------------------------

        self.icon = ttk.Label(
            self.frame,
            text="—",
            font=(
                FONT_FAMILY,
                20
            ),
            anchor="center"
        )

        self.icon.pack(
            fill="x",
            pady=(8, 4)
        )

        # --------------------------------
        # Temperature
        # --------------------------------

        self.temperature = ttk.Label(
            self.frame,
            text="—",
            font=(
                FONT_FAMILY,
                14,
                "bold"
            ),
            style="WeatherMetric.TLabel",
            anchor="center"
        )

        self.temperature.pack(
            fill="x"
        )

        # --------------------------------
        # Precipitation
        # --------------------------------

        self.precipitation = ttk.Label(
            self.frame,
            text="—",
            font=(
                FONT_FAMILY,
                8
            ),
            style="WeatherSecondary.TLabel",
            anchor="center"
        )

        self.precipitation.pack(
            fill="x",
            pady=(4, 0)
        )

    # --------------------------------
    # Update
    # --------------------------------

    def update(
        self,
        daily
    ):

        self.day.config(
            text=self.format_day(
                daily.date
            )
        )

        self.icon.config(
            text=self.get_weather_symbol(
                daily.weather_code
            )
        )

        max_temp = daily.temperature_max
        min_temp = daily.temperature_min

        if (
            max_temp is not None
            and min_temp is not None
        ):

            self.temperature.config(
                text=(
                    f"{max_temp:.0f}° "
                    f"/ "
                    f"{min_temp:.0f}°"
                )
            )

        else:

            self.temperature.config(
                text="—"
            )

        if daily.precipitation_probability is not None:

            self.precipitation.config(
                text=(
                    f"Rain "
                    f"{daily.precipitation_probability:.0f}%"
                )
            )

        else:

            self.precipitation.config(
                text="—"
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
            padx=4,
            pady=4,
            sticky="nsew"
        )

    # --------------------------------
    # Day formatting
    # --------------------------------

    @staticmethod
    def format_day(
        value
    ):

        if not value:

            return "—"

        try:

            from datetime import datetime

            date = datetime.fromisoformat(
                value
            )

            return date.strftime(
                "%a"
            ).upper()

        except (
            ValueError,
            TypeError
        ):

            return value

    # --------------------------------
    # Weather symbol
    # --------------------------------

    @staticmethod
    def get_weather_symbol(
        weather_code
    ):

        symbols = {

            0: "☀️",

            1: "🌤️",
            2: "⛅",
            3: "☁️",

            45: "🌫️",
            48: "🌫️",

            51: "🌦️",
            53: "🌦️",
            55: "🌧️",

            56: "🌧️",
            57: "🌧️",

            61: "🌧️",
            63: "🌧️",
            65: "🌧️",

            66: "🌧️",
            67: "🌧️",

            71: "🌨️",
            73: "🌨️",
            75: "❄️",

            77: "❄️",

            80: "🌦️",
            81: "🌦️",
            82: "🌧️",

            85: "🌨️",
            86: "🌨️",

            95: "⛈️",
            96: "⛈️",
            99: "⛈️",
        }

        return symbols.get(
            weather_code,
            "—"
        )

# ==============================================
# Daily Forecast
# ==============================================

class DailyForecastSection(
    WeatherSection
):

    CARD_WIDTH = 160

    def __init__(
        self,
        parent
    ):

        super().__init__(
            parent,
            "Daily Forecast"
        )

        self.cards = []

        # --------------------------------
        # Horizontal scrolling
        # --------------------------------

        self.canvas = Canvas(
            self.content,
            highlightthickness=0,
            borderwidth=0
        )

        self.scrollbar = ttk.Scrollbar(
            self.content,
            orient="horizontal",
            command=self.canvas.xview
        )

        self.canvas.configure(
            xscrollcommand=self.scrollbar.set
        )

        self.canvas.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.scrollbar.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.content.columnconfigure(
            0,
            weight=1
        )

        self.content.rowconfigure(
            0,
            weight=0
        )

        # --------------------------------
        # Scrollable card area
        # --------------------------------

        self.card_container = ttk.Frame(
            self.canvas
        )

        self.canvas_window = (
            self.canvas.create_window(
                0,
                0,
                window=self.card_container,
                anchor="nw"
            )
        )

        self.card_container.bind(
            "<Configure>",
            self._update_scrollregion
        )

        self.canvas.bind(
            "<Configure>",
            self._on_canvas_resize
        )

    # --------------------------------
    # Update
    # --------------------------------

    def update(
        self,
        daily_forecast
    ):

        # --------------------------------
        # Remove existing cards
        # --------------------------------

        for card in self.cards:

            card.frame.destroy()

        self.cards.clear()

        # --------------------------------
        # Create cards
        # --------------------------------

        for daily in daily_forecast[:7]:

            card = DailyForecastCard(
                self.card_container
            )

            card.update(
                daily
            )

            self.cards.append(
                card
            )

        self.responsive_layout()

    # --------------------------------
    # Responsive layout
    # --------------------------------

    def responsive_layout(
        self,
        width=None
    ):

        # --------------------------------
        # Configure card columns
        # --------------------------------

        for column in range(7):

            self.card_container.columnconfigure(
                column,
                weight=1,
                minsize=self.CARD_WIDTH,
                uniform="daily_card"
            )

        # --------------------------------
        # Configure row
        # --------------------------------

        self.card_container.rowconfigure(
            0,
            weight=0
        )

        # --------------------------------
        # Place cards
        # --------------------------------

        for index, card in enumerate(
            self.cards
        ):

            card.grid(
                0,
                index
            )

        self.card_container.update_idletasks()

        self._sync_canvas_window()

        self._update_scrollregion()

    # --------------------------------
    # Update scroll region
    # --------------------------------

    def _update_scrollregion(
        self,
        event=None
    ):

        self.canvas.configure(
            scrollregion=self.canvas.bbox(
                "all"
            )
        )

    # --------------------------------
    # Sync canvas window
    # --------------------------------

    def _sync_canvas_window(
        self
    ):

        content_width = (
            self.card_container.winfo_reqwidth()
        )

        content_height = (
            self.card_container.winfo_reqheight()
        )

        canvas_width = (
            self.canvas.winfo_width()
        )

        window_width = max(
            canvas_width,
            content_width
        )

        self.canvas.itemconfigure(
            self.canvas_window,
            width=window_width,
            height=content_height
        )

        self.canvas.configure(
            height=content_height
        )

    # --------------------------------
    # Canvas resize
    # --------------------------------

    def _on_canvas_resize(
        self,
        event
    ):

        content_width = (
            self.card_container.winfo_reqwidth()
        )

        canvas_width = max(
            event.width,
            content_width
        )

        self.canvas.itemconfigure(
            self.canvas_window,
            width=canvas_width
        )

        self._update_scrollregion()

# ==============================================
# Current Conditions
# ==============================================

class CurrentConditionsSection(
    WeatherSection
):

    def __init__(self, parent):

        super().__init__(
            parent,
            "Current Conditions"
        )

        self.condition = WeatherMetric(
            self.content,
            "Condition"
        )

        self.temperature = WeatherMetric(
            self.content,
            "Temperature"
        )

        self.feels_like = WeatherMetric(
            self.content,
            "Feels Like"
        )

        self.humidity = WeatherMetric(
            self.content,
            "Humidity"
        )

        self.dew_point = WeatherMetric(
            self.content,
            "Dew Point"
        )

        self.cloud_cover = WeatherMetric(
            self.content,
            "Cloud Cover"
        )

        self.visibility = WeatherMetric(
            self.content,
            "Visibility"
        )

        self.pressure = WeatherMetric(
            self.content,
            "Pressure"
        )

        self.metrics = [
            self.condition,
            self.temperature,
            self.feels_like,
            self.humidity,
            self.dew_point,
            self.cloud_cover,
            self.visibility,
            self.pressure,
        ]

    # --------------------------------
    # Update
    # --------------------------------

    def update(
        self,
        weather
    ):

        self.condition.set_value(
            weather.weather_description
        )

        self.temperature.set_value(
            f"{weather.temperature:.1f} °C"
        )

        self.feels_like.set_value(
            f"{weather.feels_like:.1f} °C"
        )

        self.humidity.set_value(
            f"{weather.humidity:.0f}%"
        )

        self.dew_point.set_value(
            f"{weather.dew_point:.1f} °C"
        )

        self.cloud_cover.set_value(
            f"{weather.cloud_cover:.0f}%"
        )

        visibility_km = (
            weather.visibility / 1000
        )

        self.visibility.set_value(
            f"{visibility_km:.1f} km"
        )

        self.pressure.set_value(
            f"{weather.surface_pressure:.0f} hPa"
        )


# ==============================================
# Wind
# ==============================================

class WindSection(
    WeatherSection
):

    def __init__(self, parent):

        super().__init__(
            parent,
            "Wind"
        )

        self.direction = WeatherMetric(
            self.content,
            "Direction"
        )

        self.speed = WeatherMetric(
            self.content,
            "Speed"
        )

        self.gusts = WeatherMetric(
            self.content,
            "Gusts"
        )

        self.metrics = [
            self.direction,
            self.speed,
            self.gusts,
        ]

    # --------------------------------
    # Update
    # --------------------------------

    def update(
        self,
        weather
    ):

        direction = degrees_to_compass(
            weather.wind_direction
        )

        self.direction.set_value(
            f"{weather.wind_direction:.0f}° {direction}"
        )

        self.speed.set_value(
            f"{weather.wind_speed:.1f} km/h"
        )

        self.gusts.set_value(
            f"{weather.wind_gusts:.1f} km/h"
        )


# ==============================================
# Precipitation
# ==============================================

class PrecipitationSection(
    WeatherSection
):

    def __init__(self, parent):

        super().__init__(
            parent,
            "Precipitation"
        )

        self.precipitation = WeatherMetric(
            self.content,
            "Precipitation"
        )

        self.rain = WeatherMetric(
            self.content,
            "Rain"
        )

        self.metrics = [
            self.precipitation,
            self.rain,
        ]

    # --------------------------------
    # Update
    # --------------------------------

    def update(
        self,
        weather
    ):

        self.precipitation.set_value(
            f"{weather.precipitation:.1f} mm"
        )

        self.rain.set_value(
            f"{weather.rain:.1f} mm"
        )


# ==============================================
# Air Quality
# ==============================================

class AirQualitySection(
    WeatherSection
):

    def __init__(self, parent):

        super().__init__(
            parent,
            "Air Quality"
        )

        self.aqi = WeatherMetric(
            self.content,
            "AQI"
        )

        self.category = WeatherMetric(
            self.content,
            "Status"
        )

        self.pm25 = WeatherMetric(
            self.content,
            "PM2.5"
        )

        self.pm10 = WeatherMetric(
            self.content,
            "PM10"
        )

        self.ozone = WeatherMetric(
            self.content,
            "O₃"
        )

        self.no2 = WeatherMetric(
            self.content,
            "NO₂"
        )

        self.so2 = WeatherMetric(
            self.content,
            "SO₂"
        )

        self.co = WeatherMetric(
            self.content,
            "CO"
        )

        self.metrics = [
            self.aqi,
            self.category,
            self.pm25,
            self.pm10,
            self.ozone,
            self.no2,
            self.so2,
            self.co,
        ]

    # --------------------------------
    # Update
    # --------------------------------

    def update(
        self,
        weather
    ):

        if weather.aqi is not None:

            self.aqi.set_value(
                f"{weather.aqi:.0f}"
            )

        else:

            self.aqi.set_value(
                "—"
            )

        self.category.set_value(
            weather.aqi_category or "—"
        )

        self.pm25.set_value(
            self.format_pollutant(
                weather.pm25
            )
        )

        self.pm10.set_value(
            self.format_pollutant(
                weather.pm10
            )
        )

        self.ozone.set_value(
            self.format_pollutant(
                weather.ozone
            )
        )

        self.no2.set_value(
            self.format_pollutant(
                weather.nitrogen_dioxide
            )
        )

        self.so2.set_value(
            self.format_pollutant(
                weather.sulphur_dioxide
            )
        )

        self.co.set_value(
            self.format_pollutant(
                weather.carbon_monoxide
            )
        )

    # --------------------------------
    # Format pollutant
    # --------------------------------

    @staticmethod
    def format_pollutant(
        value
    ):

        if value is None:

            return "—"

        return f"{value:.1f} μg/m³"


# ==============================================
# Sun & UV
# ==============================================

class SunUVSection(
    WeatherSection
):

    def __init__(self, parent):

        super().__init__(
            parent,
            "Sun & UV"
        )

        self.uv = WeatherMetric(
            self.content,
            "UV Index"
        )

        self.sunrise = WeatherMetric(
            self.content,
            "Sunrise"
        )

        self.sunset = WeatherMetric(
            self.content,
            "Sunset"
        )

        self.metrics = [
            self.uv,
            self.sunrise,
            self.sunset,
        ]

    # --------------------------------
    # Update
    # --------------------------------

    def update(
        self,
        weather
    ):

        self.uv.set_value(
            f"{weather.uv_index:.1f}"
        )

        self.sunrise.set_value(
            self.format_time(
                weather.sunrise
            )
        )

        self.sunset.set_value(
            self.format_time(
                weather.sunset
            )
        )

    # --------------------------------
    # Format ISO time
    # --------------------------------

    @staticmethod
    def format_time(
        value
    ):

        if not value:

            return "—"

        try:

            return value.split("T")[1]

        except (
            IndexError,
            AttributeError
        ):

            return value