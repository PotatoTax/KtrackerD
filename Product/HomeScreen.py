import calendar
import tkinter as tk
from tkinter import ttk

import DayObject
import ActivityBoxObject
import main
import StatisticsTools


class HomeScreen(tk.Frame):

    def __init__(self, parent, controller):

        # Creates and sets up frame
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.name = 'Home'

        # Used for storing and naming Day frames
        self.days = []
        self.day_names = [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

        self.current_week = 0

        # Initialize Widgets
        refresh_button = ttk.Button(self, text='Refresh', command=lambda: self.refresh(0))
        last_week_button = ttk.Button(self, text='Last Week', command=lambda: self.refresh(-1))
        next_week_button = ttk.Button(self, text='Next Week', command=lambda: self.refresh(1))

        # Place Widgets
        refresh_button.grid(column=0, row=0, sticky='w')
        last_week_button.grid(column=12, row=0, sticky='w')
        next_week_button.grid(column=13, row=0, sticky='w')

        # Creates a Day frame for each day of the week
        for d in range(7):
            self.days.append(
                DayObject.Day(self, d, self.day_names[d])
            )

        # Loads activities into Day frames
        self.refresh(0)

    def refresh(self, offset):

        # Adjusts the offset based on button pressed
        self.current_week += offset

        # Wipes previous activities
        for d in self.days:
            for widget in d.winfo_children():
                widget.destroy()

        # Sets up Day frames
        for d in self.days:
            d.grid(column=d.day*2, columnspan=2, row=1, sticky='n')
            d.grid_rowconfigure(0, weight=1)
            d.grid_columnconfigure(0, weight=1)
            d.title = tk.Label(d, text=d.day_name)
            d.title.grid(column=0, row=0)

        # Gets the user's activities from the current week
        activities = StatisticsTools.get_this_week(
            main.currentUser,
            self.current_week
        )

        # Places the activities based on which day they occurred on
        count = 1
        for a in activities:
            # Creates an ActivityBox frame in the correct Day frame
            box = ActivityBoxObject.ActivityBox(
                self.weekday(a.id),
                a
            )
            box.grid(column=0, row=count, ipadx=3, ipady=3, padx=3, pady=3)
            count += 1

    def weekday(self, stamp):
        # Returns the Day frame the activity should be placed in
        # Parses time stamp
        day_parts = stamp.split()[0].split('-')
        day = calendar.weekday(
            int(day_parts[0]),
            int(day_parts[1]),
            int(day_parts[2]))
        frame = self.days[day]
        return frame
