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
            self.frame,
            style="WeatherCard.TFrame"
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