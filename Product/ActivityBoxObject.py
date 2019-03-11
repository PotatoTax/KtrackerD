import tkinter as tk
from tkinter import ttk

import EditActivityWindow
import main
import SheetTools


class ActivityBox(tk.Frame):

    def __init__(self, parent, a):

        # Initializes frame
        tk.Frame.__init__(self, parent)
        self.configure(background='white')

        # Fonts used in frame
        self.fonts = {
            'ActivityTitle': ('Roboto', '20', 'bold'),
            'Username': ('Roboto', '14', 'bold'),
            'Labels': ('Roboto', '12'),
            'EditButton': ('Roboto', '8')
        }

        # Compiles all necessary information
        self.activity = a
        self.sport = a.sport
        self.title = a.title
        self.time = float(a.time)
        self.distance = float(a.distance)
        self.description = a.description
        self.id = a.id
        self.name = SheetTools.get_name(main.currentUser)

        # For skis, distance in km, pace in min/km
        if self.sport == 'Ski':
            self.distance = self.distance * 1.60934
            self.pace = self.time / self.distance
            seconds = int((self.pace % 1) * 60)
            minutes = int(self.pace - (self.pace % 1))
            self.pace = str(minutes) + ':' + str(seconds) + " /km"
            self.distance = str(round(self.distance, 2)) + " km"

        # For runs, distance in mi, pace in min/mi
        elif self.sport == 'Run':
            self.pace = self.time / self.distance
            seconds = int((self.pace % 1) * 60)
            minutes = int(self.pace)
            self.pace = str(minutes) + ':' + str(seconds) + " /mi"
            self.distance = str(round(self.distance, 2)) + " mi"

        # for rides, distance in mi, pace in mph
        elif self.sport == 'Bike':
            self.pace = self.distance / (self.time / 60)
            self.pace = str(round(self.pace, 2)) + " mph"
            self.distance = str(round(self.distance, 2)) + " mi"

        # Parses time into h:m or m:s
        self.minutes = self.time
        if self.minutes >= 60:
            self.hours = self.minutes // 60
            self.minutes -= self.hours * 60
            self.time = str(int(self.hours)) + 'h ' + str(int(self.minutes)) + 'm'
        else:
            self.seconds = int((self.minutes % 1) * 60)
            self.time = str(int(self.minutes)) + 'm ' + str(self.seconds) + 's'

        # Initialize Widgets
        self.time_text = tk.Label(self, text=self.time, bg='white')
        self.distance_text = tk.Label(self, text=self.distance, bg='white')
        self.description_text = tk.Label(self, text=self.description, bg='white')
        self.pace_text = tk.Label(self, text=self.pace, bg='white')
        self.title_text = tk.Label(self, text=self.title, font=self.fonts['ActivityTitle'], bg='white')

        self.distance_label = tk.Label(self, text='Distance', font=self.fonts['Labels'], bg='white')
        self.pace_label = tk.Label(self, text='Pace', font=self.fonts['Labels'], bg='white')
        self.time_label = tk.Label(self, text='Time', font=self.fonts['Labels'], bg='white')

        self.delete_button = ttk.Button(
            self,
            text='Edit Activity',
            command=lambda: EditActivityWindow.EditActivityWindow(self.activity)
        )

        # Place Widgets
        self.time_label.grid(column=2, row=3, sticky='w')
        self.distance_label.grid(column=0, row=3, sticky='w')
        self.pace_label.grid(column=1, row=3, sticky='w')
        self.title_text.grid(column=0, columnspan=2, row=1, sticky='w')

        self.description_text.grid(column=0, columnspan=3, row=2, sticky='w')
        self.distance_text.grid(column=0, row=4, sticky='w')
        self.pace_text.grid(column=1, row=4, sticky='w')
        self.time_text.grid(column=2, row=4, sticky='w')

        self.delete_button.grid(column=0, columnspan=3, row=5, pady=3)
