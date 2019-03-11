import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import ActivityDataObject


class AddActivityScreen(tk.Frame):

    def __init__(self, parent, controller):

        # Creates and configures frame
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.name = 'Add Activity'

        # Values for user selections
        self.sports = ['Ski', 'Run', 'Bike']
        self.units = ['miles', 'yards', 'kilometers', 'meters']
        self.months = [
            'January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December'
        ]
        self.days = [a for a in range(1, 32)]
        self.years = [a for a in range(current_year(), 1970, -1)]

        # Initialize Widgets
        self.distance_label = tk.Label(self, text='Distance')
        self.duration_label = tk.Label(self, text='Duration')
        self.sport_label = tk.Label(self, text='Sport')
        self.title_label = tk.Label(self, text='Title')
        self.description_label = tk.Label(self, text='Description')
        self.date_label = tk.Label(self, text='Date')

        self.distance_input = tk.Entry(self)
        self.duration_input = tk.Entry(self)
        self.unit_input = ttk.Combobox(self, values=self.units, state='readonly', width=10)
        self.unit_input.set(self.units[0])
        self.sport_input = ttk.Combobox(self, values=self.sports, state="readonly", width=10)
        self.sport_input.set(self.sports[0])
        self.title_input = tk.Entry(self)
        self.description_input = tk.Text(self, height=5, width=40, wrap='word')
        self.month_input = ttk.Combobox(self, values=self.months, state='readonly', width=10)
        self.month_input.set(current_month(self))
        self.day_input = ttk.Combobox(self, values=self.days, width=3)
        self.day_input.set(current_day())
        self.year_input = ttk.Combobox(self, values=self.years, width=5)
        self.year_input.set(current_year())

        self.create = ttk.Button(
            self,
            text='Create',
            command=lambda:
                 self.add_activity(
                     [
                        self.sport_input.get(),
                        self.title_input.get(),
                        self.duration_input.get(),
                        self.distance_input.get(),
                        self.description_input.get('1.0', tk.END)[:-1],
                        self.day_input.get(),
                        self.month_input.get(),
                        self.year_input.get(),
                        self.unit_input.get()
                     ]
                 )
        )
        self.cancel = ttk.Button(self, text='Cancel', command=self.clear)

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

    def clear(self):
        # Resets all inputs after an activity is submitted
        self.distance_input.delete(0, len(self.distance_input.get()))
        self.duration_input.delete(0, len(self.duration_input.get()))
        self.sport_input.delete(0, len(self.sport_input.get()))
        self.sport_input.set(self.sports[0])
        self.title_input.delete(0, len(self.title_input.get()))
        self.description_input.delete('1.0', tk.END)
        self.unit_input.set(self.units[0])
        self.year_input.set(current_year())
        self.month_input.set(current_month(self))
        self.day_input.set(current_day())

    def add_activity(self, a):

        # Used to verify date selections
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

        # Parses date input into valid timestamp
        a[5] = str(a[7]) + '-' + str(month_days[a[6]][0]) + '-' + str(a[5])

        # Checks if time input is float
        try:
            a[2] = round(float(a[2]), 2)
        except ValueError:
            self.duration_input.delete(
                0,
                len(self.duration_input.get())
            )
            messagebox.showerror('Error', 'Invalid time value')
            return 1

        # Checks if distance input is float
        try:
            a[3] = round(float(a[3]), 2)
        except ValueError:
            self.distance_input.delete(
                0,
                len(self.distance_input.get())
            )
            messagebox.showerror('Error', 'Invalid distance value')
            return 1

        # Checks if a title has been added
        if not a[1]:
            messagebox.showerror('Error', 'Please input a title')
            return 1

        # Converts any units to miles
        if a[8] == 'yards':
            a[3] = round(a[3] / 1760, 2)
        if a[8] == 'kilometers':
            a[3] = round(a[3] / 1.60934, 2)
        if a[8] == 'meters':
            a[3] = round(a[3] / 1609.34, 2)

        # Converts array into ActivityData object
        a = ActivityDataObject.ActivityData(a)

        # Adds the activity to the database
        a.add()

        self.clear()


# All parse current timestamp and return desired part
def current_day():
    today = str(datetime.datetime.today())
    today = int(today.split()[0].split('-')[2])

    return today


def current_month(self):
    today = str(datetime.datetime.today())
    today = int(today.split()[0].split('-')[1])
    month = self.months[today-1]

    return month


def current_year():
    today = str(datetime.datetime.today())
    today = int(today.split()[0].split('-')[0])

    return today
