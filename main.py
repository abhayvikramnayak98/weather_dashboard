import tkinter as tk

from ui.main_window import MainWindow
from utils.theme import configure_theme


def main():

    root = tk.Tk()

    configure_theme(root)

    MainWindow(root)

    root.mainloop()


if __name__ == "__main__":
    main()