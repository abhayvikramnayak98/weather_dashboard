import threading
import time
import tkinter as tk
from tkinter import ttk

from api.geocoding import search_locations
from config.settings import SEARCH_DEBOUNCE_MS


class SearchBar:

    def __init__(
        self,
        parent,
        on_location_selected
    ):

        self.parent = parent

        self.on_location_selected = (
            on_location_selected
        )

        self.search_after_id = None

        self.locations = []

        self.search_generation = 0

        self.build_ui()

    # --------------------------------
    # Build UI
    # --------------------------------

    def build_ui(self):

        self.frame = ttk.Frame(
            self.parent
        )

        self.frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.search_label = ttk.Label(
            self.frame,
            text="Search city:"
        )

        self.search_label.pack(
            side="left"
        )

        self.search_var = tk.StringVar()

        self.search_entry = ttk.Entry(
            self.frame,
            textvariable=self.search_var,
            width=40
        )

        self.search_entry.pack(
            side="left",
            padx=10
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.on_text_changed
        )

        self.search_entry.bind(
            "<Down>",
            self.focus_results
        )

        self.search_entry.bind(
            "<Return>",
            self.select_first_result
        )

        self.search_entry.bind(
            "<Escape>",
            self.clear_results
        )

        # --------------------------------
        # Results list
        # --------------------------------

        self.results_list = tk.Listbox(
            self.parent,
            height=5,
            width=70,
            activestyle="none",
            selectmode=tk.SINGLE,
            relief="solid",
            borderwidth=1,
            highlightthickness=0
        )

        # Hide initially.
        self.results_list.pack_forget()

        self.results_list.bind(
            "<Double-Button-1>",
            self.select_location
        )

        self.results_list.bind(
            "<Return>",
            self.select_location
        )

        self.results_list.bind(
            "<Escape>",
            self.return_to_search
        )

    # --------------------------------
    # Search input
    # --------------------------------

    def on_text_changed(self, event=None):

        query = (
            self.search_var
            .get()
            .strip()
        )

        if self.search_after_id is not None:

            self.parent.after_cancel(
                self.search_after_id
            )

            self.search_after_id = None

        self.clear_results()

        if len(query) < 2:

            return

        self.search_generation += 1

        generation = (
            self.search_generation
        )

        self.search_after_id = (
            self.parent.after(
                SEARCH_DEBOUNCE_MS,
                lambda: self.start_search(
                    query,
                    generation
                )
            )
        )

    # --------------------------------
    # Background search
    # --------------------------------

    def start_search(
        self,
        query,
        generation
    ):

        search_started = time.perf_counter()
        print()
        print("========== SEARCH DEBUG ==========")
        print(
            f"Search started: {search_started:.4f}"
        )
        thread = threading.Thread(
            target=self.search_worker,
            args=(
                query,
                generation,
                search_started
            ),
            daemon=True
        )

        thread.start()

    def search_worker(
        self,
        query,
        generation,
        search_started
    ):

        try:

            api_started = time.perf_counter()

            print(
                f"API started:   {api_started:.4f}"
            )

            locations = search_locations(
                query
            )

            api_finished = time.perf_counter()

            print(
                f"API finished:  {api_finished:.4f}"
            )

            print(
                f"API time:      "
                f"{api_finished - api_started:.3f} seconds"
            )

            print(
                f"Total search:  "
                f"{api_finished - search_started:.3f} seconds"
            )

            print("==================================")

            self.parent.after(
                0,
                lambda: self.search_complete(
                    locations,
                    generation
                )
            )

        except Exception as error:

            self.parent.after(
                0,
                lambda: self.search_error(
                    error,
                    generation
                )
            )

    # --------------------------------
    # Search result handling
    # --------------------------------

    def search_complete(
        self,
        locations,
        generation
    ):

        if generation != self.search_generation:

            return

        self.locations = locations

        self.display_results()

    def search_error(
        self,
        error,
        generation
    ):

        if generation != self.search_generation:

            return

        print(
            f"Search error: {error}"
        )

    def display_results(self):

        self.results_list.delete(
            0,
            tk.END
        )

        if not self.locations:

            self.results_list.pack_forget()

            return

        for location in self.locations:

            self.results_list.insert(
                tk.END,
                location.display_name
            )

        # Show the dropdown.
        self.results_list.pack(
            fill="x",
            padx=20,
            pady=(0, 5)
        )

        self.results_list.selection_set(
            0
        )

    # --------------------------------
    # Keyboard navigation
    # --------------------------------

    def focus_results(
        self,
        event=None
    ):

        if not self.locations:

            return "break"

        self.results_list.focus_set()

        self.results_list.selection_clear(
            0,
            tk.END
        )

        self.results_list.selection_set(
            0
        )

        self.results_list.activate(
            0
        )

        return "break"

    def select_first_result(
        self,
        event=None
    ):

        if not self.locations:

            return "break"

        self.results_list.selection_clear(
            0,
            tk.END
        )

        self.results_list.selection_set(
            0
        )

        self.select_location()

        return "break"

    # --------------------------------
    # Location selection
    # --------------------------------

    def select_location(
        self,
        event=None
    ):

        selection = (
            self.results_list.curselection()
        )

        if not selection:

            return "break"

        index = selection[0]

        location = self.locations[index]

        self.on_location_selected(
            location
        )

        self.clear_results()

        return "break"

    # --------------------------------
    # Clear results
    # --------------------------------

    def clear_results(
        self,
        event=None
    ):

        self.results_list.delete(
            0,
            tk.END
        )

        self.locations = []

        # Important:
        # hide the empty dropdown.
        self.results_list.pack_forget()

    # --------------------------------
    # Return to search
    # --------------------------------

    def return_to_search(
        self,
        event=None
    ):

        self.search_entry.focus_set()

        return "break"