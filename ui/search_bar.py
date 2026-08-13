import threading
import time
import tkinter as tk
from tkinter import ttk

from api.geocoding import search_locations
from config.settings import (
    SEARCH_DEBOUNCE_MS,
    FONT_FAMILY
)


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
        self.last_query = ""
        self.active_query = None

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
            pady=(0, 2)
        )

        self.search_label = ttk.Label(
            self.frame,
            text="Search city:",
            font=(FONT_FAMILY, 11)
        )

        self.search_label.pack(
            side="left"
        )

        self.search_var = tk.StringVar()

        self.search_entry = ttk.Entry(
            self.frame,
            textvariable=self.search_var,
            width=40,
            font=(FONT_FAMILY, 11)
        )

        self.search_entry.pack(
            side="left",
            padx=(8, 0)
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

        self.results_list = ttk.Treeview(
            self.parent,
            columns=("location",),
            show="tree",
            height=1,
            selectmode="browse"
        )

        self.results_list.column(
            "#0",
            width=0,
            stretch=False
        )

        self.results_list.column(
            "location",
            anchor="w",
            stretch=True
        )

        self.results_list.heading(
            "location",
            text=""
        )

        self.results_list.tag_configure(
            "normal",
            font=(FONT_FAMILY, 10)
        )

        self.results_list.tag_configure(
            "highlighted",
            font=(FONT_FAMILY, 10, "bold")
        )

        # Hide initially.
        self.results_list.pack_forget()

        self.results_list.bind(
            "<<TreeviewSelect>>",
            self.on_result_highlight
        )

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

        self.results_list.bind(
            "<Up>",
            self.move_selection_up
        )

        self.results_list.bind(
            "<Down>",
            self.move_selection_down
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

        if query == self.last_query:

            return

        if self.search_after_id is not None:

            self.parent.after_cancel(
                self.search_after_id
            )

            self.search_after_id = None

        self.clear_results()

        if len(query) < 2:

            self.last_query = query

            return

        self.last_query = query

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
        # --------------------------------
        # Prevent duplicate query
        # --------------------------------

        if query == self.active_query:

            return

        self.active_query = query
        
        thread = threading.Thread(
            target=self.search_worker,
            args=(
                query,
                generation
            ),
            daemon=True
        )

        thread.start()

    def search_worker(
        self,
        query,
        generation
    ):

        try:

            locations = search_locations(
                query
            )

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

        for item in self.results_list.get_children():
            self.results_list.delete(item)

        if not self.locations:

            self.results_list.pack_forget()

            return

        for index, location in enumerate(self.locations):

            self.results_list.insert(
                "",
                "end",
                iid=str(index),
                text="",
                values=(location.display_name,),
                tags=("normal",)
            )

        # Size dropdown to the number of results,
        # with a maximum of 5 visible rows.
        result_count = min(
            len(self.locations),
            5
        )

        self.results_list.configure(
            height=result_count
        )

        self.results_list.pack(
            fill="x",
            pady=(0, 4)
        )

        # Highlight the first result.
        self.results_list.selection_set(
            "0"
        )

        self.results_list.focus(
            "0"
        )

    def on_result_highlight(self, event=None):

        selected = self.results_list.selection()

        for item in self.results_list.get_children():

            self.results_list.item(
                item,
                tags=("normal",)
            )

        if not selected:

            return

        self.results_list.item(
            selected[0],
            tags=("highlighted",)
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

        selected = self.results_list.selection()

        if not selected:

            self.results_list.selection_set(
                "0"
            )

            self.results_list.focus(
                "0"
            )

        return "break"

    def move_selection_down(
        self,
        event=None
    ):

        if not self.locations:

            return "break"

        items = self.results_list.get_children()

        if not items:

            return "break"

        selected = self.results_list.selection()

        if not selected:

            next_index = 0

        else:

            current_index = items.index(
                selected[0]
            )

            next_index = min(
                current_index + 1,
                len(items) - 1
            )

        next_item = items[next_index]

        self.results_list.selection_set(
            next_item
        )

        self.results_list.focus(
            next_item
        )

        self.results_list.see(
            next_item
        )

        return "break"


    def move_selection_up(
        self,
        event=None
    ):

        if not self.locations:

            return "break"

        items = self.results_list.get_children()

        if not items:

            return "break"

        selected = self.results_list.selection()

        if not selected:

            previous_index = 0

        else:

            current_index = items.index(
                selected[0]
            )

            previous_index = max(
                current_index - 1,
                0
            )

        previous_item = items[previous_index]

        self.results_list.selection_set(
            previous_item
        )

        self.results_list.focus(
            previous_item
        )

        self.results_list.see(
            previous_item
        )

        return "break"
    
    def move_selection_down(
        self,
        event=None
    ):

        if not self.locations:

            return "break"

        items = self.results_list.get_children()

        if not items:

            return "break"

        selected = self.results_list.selection()

        if not selected:

            next_index = 0

        else:

            current_index = items.index(
                selected[0]
            )

            next_index = min(
                current_index + 1,
                len(items) - 1
            )

        next_item = items[next_index]

        self.results_list.selection_set(
            next_item
        )

        self.results_list.focus(
            next_item
        )

        self.results_list.see(
            next_item
        )

        return "break"


    def move_selection_up(
        self,
        event=None
    ):

        if not self.locations:

            return "break"

        items = self.results_list.get_children()

        if not items:

            return "break"

        selected = self.results_list.selection()

        if not selected:

            previous_index = 0

        else:

            current_index = items.index(
                selected[0]
            )

            previous_index = max(
                current_index - 1,
                0
            )

        previous_item = items[previous_index]

        self.results_list.selection_set(
            previous_item
        )

        self.results_list.focus(
            previous_item
        )

        self.results_list.see(
            previous_item
        )

        return "break"

    def select_first_result(
        self,
        event=None
    ):

        # --------------------------------
        # Cancel pending search
        # --------------------------------

        if self.search_after_id is not None:

            self.parent.after_cancel(
                self.search_after_id
            )

            self.search_after_id = None

        # --------------------------------
        # Select first result
        # --------------------------------

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

        selection = self.results_list.selection()

        if not selection:

            return "break"

        index = int(
            selection[0]
        )

        if index < 0 or index >= len(self.locations):

            return "break"

        location = self.locations[index]

        self.active_query = None

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

        for item in self.results_list.get_children():

            self.results_list.delete(
                item
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