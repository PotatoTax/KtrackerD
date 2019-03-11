import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import ActivityDataObject


class EditActivityWindow:

    def __init__(self, a):

        self.Frame = tk.Tk()
        tk.Tk.wm_title(
            self.Frame,
            string='KTracker | Edit Activity'
        )
        self.Frame.geometry('500x250')
        self.activity = a

        # Values for user inputs
        self.sports = ['Ski', 'Run', 'Bike']
        self.units = ['miles', 'yards', 'kilometers', 'meters']
        self.months = [
            'January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December'
        ]
        self.days = [a for a in range(1, 32)]
        self.years = [a for a in range(current_year(), 1970, -1)]

        # Initializes Widgets
        self.distance_label = tk.Label(self.Frame, text='Distance')
        self.duration_label = tk.Label(self.Frame, text='Duration')
        self.sport_label = tk.Label(self.Frame, text='Sport')
        self.title_label = tk.Label(self.Frame, text='Title')
        self.description_label = tk.Label(self.Frame, text='Description')
        self.date_label = tk.Label(self.Frame, text='Date')

        self.distance_input = tk.Entry(self.Frame)
        self.distance_input.insert('0', self.activity.distance)
        self.duration_input = tk.Entry(self.Frame)
        self.duration_input.insert('0', self.activity.time)
        self.title_input = tk.Entry(self.Frame)
        self.title_input.insert('0', self.activity.title)
        self.description_input = tk.Text(self.Frame, height=5, width=40, wrap='word')
        self.description_input.insert('1.0', self.activity.description)

        self.unit_input = ttk.Combobox(self.Frame, values=self.units, state='readonly', width=10)
        self.unit_input.set(self.units[0])
        self.sport_input = ttk.Combobox(self.Frame, values=self.sports, state="readonly", width=10)
        self.sport_input.set(self.activity.sport)
        self.month_input = ttk.Combobox(self.Frame, values=self.months, state='readonly', width=10)
        self.month_input.set(self.month(self.activity.id))
        self.day_input = ttk.Combobox(self.Frame, values=self.days, width=3)
        self.day_input.set(day(self.activity.id))
        self.year_input = ttk.Combobox(self.Frame, values=self.years, width=5)
        self.year_input.set(year(self.activity.id))

        self.create = ttk.Button(
            self.Frame,
            text='Create',
            command=lambda:
            self.edit_activity(
                [
                    self.sport_input.get(),
                    self.title_input.get(),
                    self.duration_input.get(),
                    self.distance_input.get(),
                    self.description_input.get('1.0', tk.END)[:-1],
                    self.day_input.get(),
                    self.month_input.get(),
                    self.year_input.get(),
                    self.unit_input.get(),
                    self.activity
                ]
            )
        )
        self.cancel = ttk.Button(self.Frame, text='Cancel', command=lambda: self.Frame.destroy())

        # Place Widgets
        self.distance_label.grid(column=0, row=0, sticky='w')
        self.duration_label.grid(column=2, columnspan=2, row=0, sticky='w')
        self.sport_label.grid(column=4, row=0, sticky='w')
        self.title_label.grid(column=0, row=2, sticky='w')
        self.description_label.grid(column=0, row=4, sticky='w')

        self.distance_input.grid(column=0, row=1, sticky='w')
        self.unit_input.grid(column=1, row=1, sticky='w')
        self.duration_input.grid(column=2, columnspan=2, row=1, sticky='w')
        self.sport_input.grid(column=4, row=1, sticky='w')
        self.title_input.grid(column=0, row=3, sticky='w')
        self.month_input.grid(column=1, row=3, sticky='w')
        self.day_input.grid(column=2, row=3, sticky='w')
        self.year_input.grid(column=3, row=3, sticky='w')
        self.description_input.grid(column=0, columnspan=3, row=5, sticky='w')

        self.create.grid(column=0, row=6)
        self.cancel.grid(column=1, row=6)

    def month(self, timestamp):
        month = int(timestamp.split('-')[1])

        return self.months[month - 1]

    def current_month(self):
        today = str(datetime.datetime.today())
        today = int(today.split()[0].split('-')[1])

        return self.months[today - 1]

    def edit_activity(self, a):

        old_activity = a[-1]

        # Verifies day - month pairs
        month_days = {
            'January': ['01', 31],
            'February': ['02', 28],
            'March': ['03', 31],
            'April': ['04', 30],
            'May': ['05', 31],
            'June': ['06', 30],
            'July': ['07', 31],
            'August': ['08', 31],
            'September': ['09', 30],
            'October': ['10', 31],
            'November': ['11', 30],
            'December': ['12', 31]
        }
        if not int(a[5]) <= month_days[a[6]][1]:
            messagebox.showerror(
                'Error',
                'Invalid day : ' + a[5] + ' for month : ' + a[6]
            )
            return 1

        # Parses date into valid timestamp
        a[5] = str(a[7]) + '-' + str(month_days[a[6]][0]) + '-' + str(a[5])

        # Ensures that time is float
        try:
            a[2] = round(float(a[2]), 2)
        except ValueError:
            self.duration_input.delete(
                0,
                len(self.duration_input.get())
            )
            messagebox.showerror(
                'Error',
                'Invalid time value'
            )
            return 1

        # Ensures that distance is float
        try:
            a[3] = round(float(a[3]), 2)
        except ValueError:
            self.distance_input.delete(
                0,
                len(self.distance_input.get())
            )
            messagebox.showerror(
                'Error',
                'Invalid distance value'
            )
            return 1

        # Ensures that a title was added
        if not a[1]:
            messagebox.showerror(
                'Error',
                'Please input a title'
            )
            return 1

        # Converts all units to miles
        if a[8] == 'yards':
            a[3] = round(a[3] / 1760, 2)
        if a[8] == 'kilometers':
            a[3] = round(a[3] / 1.60934, 2)
        if a[8] == 'meters':
            a[3] = round(a[3] / 1609.34, 2)

        # Converts activity to ActivityData object
        a = ActivityDataObject.ActivityData(a)

        # Edits the database record of the activity and closes the window
        a.edit(old_activity)

        self.Frame.destroy()


def day(timestamp):
    return int(timestamp.split('-')[2])


def year(timestamp):
    return int(timestamp.split('-')[0])


def current_year():
    today = str(datetime.datetime.today())
    return int(today.split()[0].split('-')[0])
