"""Test Module."""
import tkinter as tk
from lib import Page, PageManager


class LoginPage(Page):
    """Example class."""

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is the login page")
        label.pack()

        btn = tk.Button(self, text="Should also go to reservation",
                        command=lambda: self.pages.goto("reserve"))
        btn.pack()


class ReservePage(Page):
    """Example class."""

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is the reservation page")
        label.pack()

        btn = tk.Button(self, text="Should go to login",
                        command=lambda: self.pages.goto("login"))
        btn.pack()


if __name__ == "__main__":
    root = tk.Tk()
    main = PageManager(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x800")

    main.add_page("login", LoginPage)
    main.add_page("reserve", ReservePage)

    main.goto("login")

    root.mainloop()
