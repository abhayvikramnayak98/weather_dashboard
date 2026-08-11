from tkinter import ttk

from config.settings import FONT_FAMILY


class WeatherSection:

    def __init__(
        self,
        parent,
        title,
    ):

        self.parent = parent
        self.title = title

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
    # Responsive metric layout
    # --------------------------------

    def layout_metrics(self, columns):

        for metric in self.metrics:

            metric.frame.grid_forget()

        for column in range(columns):

            self.content.columnconfigure(
                column,
                weight=1,
                uniform="metric"
            )

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
    # Determine metric columns
    # --------------------------------

    def responsive_layout(self, width):

        if width >= 900:

            columns = 4

        elif width >= 600:

            columns = 2

        else:

            columns = 1

        self.layout_metrics(
            columns
        )

class WeatherMetric:

    def __init__(
        self,
        parent,
        label,
        value="—",
    ):

        self.frame = ttk.Frame(
            parent,
            style="WeatherCard.TFrame"
        )

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

        self.value = ttk.Label(
            self.frame,
            text=value,
            font=(
                FONT_FAMILY,
                12,
                "bold"
            ),
            style="WeatherMetric.TLabel",
            anchor="w"
        )

        self.value.pack(
            fill="x",
            pady=(3, 0)
        )

    def set_value(
        self,
        value
    ):

        self.value.config(
            text=value
        )

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

class CurrentConditionsSection(WeatherSection):

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

class WindSection(WeatherSection):

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

class PrecipitationSection(WeatherSection):

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

class AirQualitySection(WeatherSection):

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
            "Ozone"
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

class SunUVSection(WeatherSection):

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