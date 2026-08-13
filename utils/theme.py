from datetime import datetime
from tkinter import ttk


# --------------------------------
# Light theme
# --------------------------------

LIGHT_THEME = {
    "background": "#F4F7FB",
    "surface": "#FFFFFF",
    "border": "#DCE3EC",
    "primary": "#1E3A5F",
    "text": "#17212B",
    "secondary": "#667085",
    "accent": "#3B82F6",
}


# --------------------------------
# Dark theme
# --------------------------------

DARK_THEME = {
    "background": "#101820",
    "surface": "#18232D",
    "border": "#2B3945",
    "primary": "#8EC5FF",
    "text": "#F1F5F9",
    "secondary": "#A8B3BF",
    "accent": "#60A5FA",
}


class ThemeManager:

    def __init__(self, root):

        self.root = root

        self.style = ttk.Style(
            root
        )

        self.style.theme_use(
            "clam"
        )

        self.current_theme = None

        self.apply_theme()

    # --------------------------------
    # Determine theme
    # --------------------------------

    def get_theme(self):

        current_hour = (
            datetime.now().hour
        )

        if 6 <= current_hour < 18:

            return "light"

        return "dark"

    # --------------------------------
    # Apply theme
    # --------------------------------

    def apply_theme(self):

        theme_name = self.get_theme()

        if theme_name == self.current_theme:

            self.schedule_check()

            return

        self.current_theme = theme_name

        if theme_name == "light":

            colors = LIGHT_THEME

        else:

            colors = DARK_THEME

        # --------------------------------
        # Classic Tkinter widgets
        # --------------------------------

        self.root.option_add(
            "*Listbox.background",
            colors["surface"]
        )

        self.root.option_add(
            "*Listbox.foreground",
            colors["text"]
        )

        self.root.option_add(
            "*Listbox.selectBackground",
            colors["accent"]
        )

        self.root.option_add(
            "*Listbox.selectForeground",
            "#FFFFFF"
        )

        self.root.option_add(
            "*Listbox.highlightBackground",
            colors["border"]
        )

        self.root.option_add(
            "*Listbox.highlightColor",
            colors["border"]
        )

        # --------------------------------
        # General
        # --------------------------------

        self.style.configure(
            ".",
            background=colors["background"],
            foreground=colors["text"],
        )

        # --------------------------------
        # Frame
        # --------------------------------

        self.style.configure(
            "TFrame",
            background=colors["background"],
        )


        # --------------------------------
        # Dashboard Info Panel
        # --------------------------------

        self.style.configure(
            "DashboardInfo.TFrame",
            background=colors["surface"],
            bordercolor=colors["border"],
            relief="solid",
            borderwidth=1,
        )

        self.style.configure(
            "DashboardLocation.TLabel",
            background=colors["surface"],
            foreground=colors["text"],
        )

        self.style.configure(
            "DashboardStatus.TLabel",
            background=colors["surface"],
            foreground=colors["secondary"],
        )


        # --------------------------------
        # Label
        # --------------------------------

        self.style.configure(
            "TLabel",
            background=colors["background"],
            foreground=colors["text"],
        )

        # --------------------------------
        # LabelFrame
        # --------------------------------

        self.style.configure(
            "TLabelFrame",
            background=colors["surface"],
            foreground=colors["primary"],
            bordercolor=colors["border"],
            relief="solid",
            borderwidth=1,
        )

        self.style.configure(
            "TLabelFrame.Label",
            background=colors["surface"],
            foreground=colors["primary"],
        )

        # --------------------------------
        # Entry
        # --------------------------------

        self.style.configure(
            "TEntry",
            fieldbackground=colors["surface"],
            foreground=colors["text"],
            bordercolor=colors["border"],
        )

        # --------------------------------
        # Button
        # --------------------------------

        self.style.configure(
            "TButton",
            background=colors["accent"],
            foreground="white",
            borderwidth=0,
            padding=(12, 6),
        )

        self.style.map(
            "TButton",
            background=[
                (
                    "active",
                    colors["primary"]
                )
            ]
        )

        # --------------------------------
        # Weather Card
        # --------------------------------

        self.style.configure(
            "WeatherCard.TFrame",
            background=colors["surface"],
            bordercolor=colors["border"],
            relief="solid",
            borderwidth=1,
        )

        # --------------------------------
        # Weather Card Title
        # --------------------------------

        self.style.configure(
            "WeatherCardTitle.TLabel",
            background=colors["surface"],
            foreground=colors["primary"],
        )

        # --------------------------------
        # Weather Card Main Value
        # --------------------------------

        self.style.configure(
            "WeatherMetric.TLabel",
            background=colors["surface"],
            foreground=colors["text"],
        )

        # --------------------------------
        # Weather Card Secondary Value
        # --------------------------------

        self.style.configure(
            "WeatherSecondary.TLabel",
            background=colors["surface"],
            foreground=colors["secondary"],
        )

        self.schedule_check()

    # --------------------------------
    # Check theme periodically
    # --------------------------------

    def schedule_check(self):

        self.root.after(
            30_000,
            self.apply_theme
        )


def configure_theme(root):

    return ThemeManager(root)