APP_TITLE = "Weather Dashboard"

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

MIN_WINDOW_WIDTH = 700
MIN_WINDOW_HEIGHT = 600

WEATHER_REFRESH_INTERVAL = 10 * 60 * 1000
SEARCH_DEBOUNCE_MS = 350

GEOCODING_URL = (
    "https://geocoding-api.open-meteo.com/v1/search"
)

WEATHER_URL = (
    "https://api.open-meteo.com/v1/forecast"
)

AIR_QUALITY_URL = (
    "https://air-quality-api.open-meteo.com/v1/air-quality"
)


# -------------------------
# Typography
# -------------------------

FONT_FAMILY = "Inter"

FONT_TITLE = (FONT_FAMILY, 24, "bold")
FONT_CLOCK = (FONT_FAMILY, 20, "bold")
FONT_LOCATION = (FONT_FAMILY, 15, "bold")
FONT_SECTION = (FONT_FAMILY, 12, "bold")
FONT_METRIC = (FONT_FAMILY, 22, "bold")
FONT_LABEL = (FONT_FAMILY, 10, "normal")
FONT_STATUS = (FONT_FAMILY, 9, "normal")
FONT_SMALL = (FONT_FAMILY, 9, "normal")

# -------------------------
# Colors
# -------------------------

COLOR_BACKGROUND = "#F4F7FB"
COLOR_SURFACE = "#FFFFFF"
COLOR_BORDER = "#DCE3EC"

COLOR_PRIMARY = "#1E3A5F"
COLOR_TEXT = "#17212B"
COLOR_TEXT_SECONDARY = "#667085"

COLOR_ACCENT = "#3B82F6"

COLOR_SUCCESS = "#15803D"
COLOR_WARNING = "#D97706"
COLOR_DANGER = "#DC2626"