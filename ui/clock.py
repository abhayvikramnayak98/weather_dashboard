import tkinter as tk
from tkinter import ttk
from datetime import datetime

from config.settings import (
    FONT_CLOCK,
    FONT_FAMILY,
)


class Clock:

    def __init__(self, parent):

        self.parent = parent

        self.clock_label = ttk.Label(
            parent,
            text="",
            font=FONT_CLOCK,
            anchor="e"
        )

        self.clock_label.grid(
            row=0,
            column=1,
            sticky="e",
            padx=(20, 0)
        )

        self.parent.columnconfigure(
            0,
            weight=1
        )

        self.parent.columnconfigure(
            1,
            weight=1
        )

        # Monitor the available header width.
        parent.bind(
            "<Configure>",
            self.on_resize
        )

        self.update_clock()

    # --------------------------------
    # Running clock
    # --------------------------------

    def update_clock(self):

        now = datetime.now()

        text = now.strftime(
            "%a, %d/%m/%Y %I:%M:%S %p"
        )

        self.clock_label.config(
            text=text
        )

        self.parent.after(
            1000,
            self.update_clock
        )

    # --------------------------------
    # Responsive font
    # --------------------------------

    def on_resize(self, event):

        width = event.width

        if width >= 1000:

            size = 20

        elif width >= 850:

            size = 17

        elif width >= 700:

            size = 14

        elif width >= 550:

            size = 11

        else:

            size = 9

        self.clock_label.config(
            font=(
                FONT_FAMILY,
                size,
                "bold"
            )
        )