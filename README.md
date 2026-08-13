# Weather Dashboard

**Version:** 1.0.0\
**Status:** Stable / Final\
**Application type:** Python desktop weather dashboard

## Overview

Weather Dashboard is a desktop application for searching for locations
and viewing current weather conditions, daily forecasts, hourly
forecasts, air-quality information, wind, precipitation, and related
weather details.

The application is organized into separate API, configuration, model,
service, UI, and utility layers to keep the codebase maintainable.

## Features

-   Location search with result highlighting
-   Keyboard navigation in the search results
-   Bold highlighting for the active search result
-   Current weather conditions
-   Daily forecast
-   Hourly forecast
-   Weather-related detail sections
-   Responsive dashboard layouts for different window sizes
-   Scrollable content where required
-   Clean separation between application logic and UI components

## Project Structure

``` text
WeatherDashboard/
├── main.py
├── requirements.txt
│
├── api/
├── config/
├── models/
├── services/
├── ui/
└── utils/
```

### Main components

-   `api/` --- Weather, geocoding, and air-quality API integration
-   `config/` --- Application configuration
-   `models/` --- Location and weather data models
-   `services/` --- Weather service logic
-   `ui/` --- Dashboard, search, forecast, cards, scrolling, and clock
    components
-   `utils/` --- Theme, compass, and weather-condition utilities

## Requirements

-   Python 3
-   Tk/Tcl support for the desktop interface
-   Internet connection for weather and location services
-   Python packages listed in `requirements.txt`

## Installation

### 1. Create a virtual environment

From the project root:

``` text
python -m venv .venv
```

### 2. Activate the environment

**Windows Command Prompt:**

``` text
.venv\Scripts\activate
```

**Windows PowerShell:**

``` text
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

``` text
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running the Application

From the project root:

``` text
python main.py
```

## Search Controls

The location search supports both mouse and keyboard interaction.

  Key / Action   Result
  -------------- ------------------------------------
  `Down`         Move to the next search result
  `Up`           Move to the previous search result
  `Enter`        Select the highlighted result
  `Esc`          Close the result list
  Mouse          Select a result

The currently highlighted search result is displayed in **bold**.

## Configuration

Application configuration is maintained in:

``` text
config/settings.py
```

Before deployment, review this file for any external-service
configuration required by the application.

Do not commit API keys, tokens, passwords, or other secrets to source
control.

## Release Hygiene

The development environment should not be included in the release.

Do not commit or distribute:

``` text
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
build/
dist/
*.egg-info/
```

The project includes a `.gitignore` file to help prevent these files
from being committed.

## Troubleshooting

### The application does not start

1.  Confirm that Python is installed.
2.  Confirm that the virtual environment is active.
3.  Install the dependencies:

``` text
python -m pip install -r requirements.txt
```

4.  Run the application from the project root:

``` text
python main.py
```

### Weather data is unavailable

-   Check the internet connection.
-   Check the application configuration.
-   Verify that the external weather/geocoding services are available.
-   Check the terminal for any error messages.

### Tkinter is unavailable

Install a Python distribution that includes Tk/Tcl support.

On Windows, the standard Python installer normally includes this
component.

## Version

### v1.0.0 --- Stable Release

This is the first stable release of the Weather Dashboard.

The release includes the completed dashboard UI, responsive layouts,
location search, keyboard search navigation, current conditions, daily
forecast, hourly forecast, and supporting weather information.

## License

See the `LICENSE` file included with the project for the applicable
license terms.

## Final Release Checklist

Before distributing the application:

-   [ ] Application launches successfully
-   [ ] Location search works
-   [ ] Mouse selection works
-   [ ] `Up` / `Down` keyboard navigation works
-   [ ] `Enter` selects the highlighted location
-   [ ] `Esc` closes the search results
-   [ ] Current conditions load
-   [ ] Daily forecast loads
-   [ ] Hourly forecast loads
-   [ ] Wide layout verified
-   [ ] Narrow layout verified
-   [ ] No development `.venv` included
-   [ ] No Python cache files included
-   [ ] Version is `1.0.0`
