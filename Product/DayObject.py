import tkinter as tk


class Day(tk.Frame):
    # Serves as a holder for ActivityBox frames on the home page

    def __init__(self, parent, day, day_name):
        tk.Frame.__init__(self, parent)

        # Assigned a numerical weekday and by name
        self.day = day
        self.day_name = day_name
