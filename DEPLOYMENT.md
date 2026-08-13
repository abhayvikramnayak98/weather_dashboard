# Deployment Guide

**Application:** Weather Dashboard\
**Version:** 1.0.0\
**Status:** Stable / Final

## 1. Purpose

This document describes the recommended procedure for installing,
verifying, and releasing Weather Dashboard v1.0.0.

The release should be prepared from a clean project checkout and should
not include the development virtual environment or Python cache files.

## 2. Project Requirements

The application requires:

-   Python 3
-   Tk/Tcl support
-   Internet access for external weather and location services
-   The dependencies listed in `requirements.txt`

## 3. Prepare a Clean Environment

Open a terminal in the project root.

Create a new virtual environment:

``` text
python -m venv .venv
```

Activate it.

### Windows Command Prompt

``` text
.venv\Scripts\activate
```

### Windows PowerShell

``` text
.\.venv\Scripts\Activate.ps1
```

Upgrade pip:

``` text
python -m pip install --upgrade pip
```

Install the project dependencies:

``` text
python -m pip install -r requirements.txt
```

## 4. Configuration

Review:

``` text
config/settings.py
```

before first launch.

Any external-service configuration required by the application must be
supplied using the mechanism supported by the project.

**Never commit API keys, access tokens, passwords, or other secrets to
source control.**

## 5. Run the Application

From the project root:

``` text
python main.py
```

The application should start without an unhandled exception.

## 6. Functional Verification

Perform the following smoke tests before distributing the release.

### Application startup

-   [ ] Application launches successfully.
-   [ ] Main dashboard appears correctly.
-   [ ] No traceback appears in the terminal.

### Location search

-   [ ] Search field accepts text.
-   [ ] Search results appear.
-   [ ] First result is visibly highlighted.
-   [ ] Highlighted result is bold.
-   [ ] Other results remain regular.
-   [ ] `Down` moves to the next result.
-   [ ] `Up` moves to the previous result.
-   [ ] `Enter` selects the highlighted result.
-   [ ] `Esc` closes the result list.
-   [ ] Mouse selection works.

### Weather dashboard

-   [ ] Current conditions load.
-   [ ] Daily forecast loads.
-   [ ] Hourly forecast loads.
-   [ ] Weather detail sections load.
-   [ ] Scrolling works where required.

### Responsive layout

Verify the application at the layouts used during final UI testing:

-   [ ] Wide layout
-   [ ] Medium layout
-   [ ] Narrow layout

Confirm that the dashboard remains usable and that no unexpected
horizontal or vertical layout problems appear.

## 7. Release Contents

A source release should contain:

``` text
main.py
requirements.txt
README.md
DEPLOYMENT.md
CHANGELOG.md
LICENSE
.gitignore

api/
config/
models/
services/
ui/
utils/
```

## 8. Files That Must Not Be Released

Do not include development or generated files such as:

``` text
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
build/
dist/
*.egg-info/
project_tree.txt
```

The `.gitignore` file is configured to help prevent common development
artifacts from being committed.

## 9. Git Release Procedure

Before committing, inspect the working tree:

``` text
git status
```

Review the files carefully.

Add the intended release files:

``` text
git add .
```

Create the release commit:

``` text
git commit -m "Release v1.0.0"
```

Create an annotated version tag:

``` text
git tag -a v1.0.0 -m "Weather Dashboard v1.0.0"
```

Verify the tag:

``` text
git tag
```

Verify the working tree:

``` text
git status
```

The working tree should be clean after the release commit.

## 10. Release Archive

If a source archive is required, create it from the clean release state.

The archive should contain the application source and release documents,
but not `.venv`, cache files, or other development artifacts.

## 11. Future Executable Packaging

If a standalone Windows executable is required later, treat that as a
separate packaging step.

Do not add a packaging dependency or build configuration to the project
merely for documentation purposes. First choose the packaging tool and
test the resulting executable on a clean Windows environment.

The v1.0.0 source release remains the authoritative baseline.

## 12. Troubleshooting

### Dependencies fail to install

Confirm that:

``` text
python --version
```

reports the expected Python installation.

Then run:

``` text
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Application imports fail

Make sure the terminal's current directory is the project root and
launch with:

``` text
python main.py
```

### Weather or location data fails

Verify:

-   Internet connectivity
-   External-service availability
-   Application configuration
-   Any credentials required by the configured services

Check the terminal output for the underlying error.

### Tkinter is unavailable

Install a Python distribution that includes Tk/Tcl support.

## 13. Final Release Checklist

Before declaring the release complete:

-   [ ] README.md present
-   [ ] DEPLOYMENT.md present
-   [ ] CHANGELOG.md present
-   [ ] LICENSE present
-   [ ] .gitignore present
-   [ ] requirements.txt present
-   [ ] Application source present
-   [ ] `.venv/` excluded
-   [ ] Python cache files excluded
-   [ ] Application starts successfully
-   [ ] Search interaction verified
-   [ ] Weather data verified
-   [ ] Responsive layouts verified
-   [ ] Git working tree clean
-   [ ] `v1.0.0` tag created

## 14. Release Identity

**Weather Dashboard v1.0.0**

This is the stable baseline for future development.
