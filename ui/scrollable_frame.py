import tkinter as tk
from tkinter import ttk


class ScrollableFrame:

    def __init__(self, parent):

        self.parent = parent

        # --------------------------------
        # Outer container
        # --------------------------------

        self.frame = ttk.Frame(
            parent
        )

        self.frame.pack(
            fill="both",
            expand=True
        )

        # --------------------------------
        # Canvas
        # --------------------------------

        self.canvas = tk.Canvas(
            self.frame,
            highlightthickness=0,
            borderwidth=0
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        # --------------------------------
        # Scrollbar
        # --------------------------------

        self.scrollbar = ttk.Scrollbar(
            self.frame,
            orient="vertical",
            command=self.canvas.yview
        )

        self.scrollbar.pack(
            side="right",
            fill="y"
        )

        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        # --------------------------------
        # Scrollable content
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

        # --------------------------------
        # Content resize
        # --------------------------------

        self.content.bind(
            "<Configure>",
            self.on_content_configure
        )

        # --------------------------------
        # Canvas resize
        # --------------------------------

        self.canvas.bind(
            "<Configure>",
            self.on_canvas_configure
        )

        # --------------------------------
        # Mouse wheel
        # --------------------------------

        self.canvas.bind(
            "<Enter>",
            self.bind_mousewheel
        )

        self.canvas.bind(
            "<Leave>",
            self.unbind_mousewheel
        )

    # --------------------------------
    # Content size changed
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
    # Canvas width changed
    # --------------------------------

    def on_canvas_configure(
        self,
        event
    ):

        self.canvas.itemconfigure(
            self.window_id,
            width=event.width
        )

    # --------------------------------
    # Bind mouse wheel
    # --------------------------------

    def bind_mousewheel(
        self,
        event=None
    ):

        self.canvas.bind_all(
            "<MouseWheel>",
            self.on_mousewheel
        )

    # --------------------------------
    # Unbind mouse wheel
    # --------------------------------

    def unbind_mousewheel(
        self,
        event=None
    ):

        self.canvas.unbind_all(
            "<MouseWheel>"
        )

    # --------------------------------
    # Mouse wheel
    # --------------------------------

    def on_mousewheel(
        self,
        event
    ):

        self.canvas.yview_scroll(
            int(
                -1 * (event.delta / 120)
            ),
            "units"
        )

    # --------------------------------
    # Scroll to top
    # --------------------------------

    def scroll_to_top(self):

        self.canvas.yview_moveto(
            0
        )