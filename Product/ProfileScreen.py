import tkinter as tk
from tkinter import ttk

import ChangePasswordWindow
import main
import StatisticsTools


class ProfileScreen(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.fonts = {
            'TitleText': ('Roboto', '25', 'bold'),
            'SportTitles': ('Roboto', '20', 'bold'),
            'Stats': ('Roboto', '15')
        }
        self.name = 'Profile'

        # Gets a Statistics object for the current user
        self.stats = StatisticsTools.generate_stats(main.currentUser)

        # Place username and change password button
        self.username_label = tk.Label(
            self,
            text=('Username : ' + main.currentUser)
        )

        self.change_pass = ttk.Button(
            self,
            text='Change Password',
            command=ChangePasswordWindow.ChangePasswordWindow
        )

        self.username_label.grid(column=0, row=0)

        self.change_pass.grid(column=0, row=1)

        # Initialize Labels
        self.stats_label = tk.Label(self, text='Statistics', font=self.fonts['TitleText'])
        self.totals_label = tk.Label(self, text='All Activities', font=self.fonts['SportTitles'])
        self.ski_label = tk.Label(self, text='Skis', font=self.fonts['SportTitles'])
        self.run_label = tk.Label(self, text='Runs', font=self.fonts['SportTitles'])
        self.bike_label = tk.Label(self, text='Rides', font=self.fonts['SportTitles'])

        # Totals Labels
        self.totals_label = tk.Label(
            self,
            text='All Activities',
            font=self.fonts['SportTitles']
        )
        self.totals_count_label = tk.Label(
            self,
            text='Count',
            font=self.fonts['Stats']
        )
        self.totals_distance_label = tk.Label(
            self,
            text='Distance (mi)',
            font=self.fonts['Stats']
        )
        self.totals_time_label = tk.Label(
            self,
            text='Time',
            font=self.fonts['Stats']
        )

        # Averages Labels
        self.averages_label = tk.Label(
            self,
            text='Averages', font=self.fonts['Stats']
        )
        self.averages_distance_label = tk.Label(
            self,
            text='Distance (mi)', font=self.fonts['Stats']
        )
        self.averages_time_label = tk.Label(
            self,
            text='Time', font=self.fonts['Stats']
        )

        # Initialize Data
        # All activities Labels
        self.total_count = tk.Label(
            self,
            text=str(self.stats.total.total_count),
            font=self.fonts['Stats']
        )
        self.total_distance = tk.Label(
            self,
            text=str(self.stats.total.total_distance),
            font=self.fonts['Stats']
        )
        self.total_time = tk.Label(
            self,
            text=str(self.stats.total.total_time),
            font=self.fonts['Stats']
        )
        self.total_average_distance = tk.Label(
            self,
            text=str(round(self.stats.total.average_distance, 2)),
            font=self.fonts['Stats']
        )
        self.total_average_time = tk.Label(
            self,
            text=str(round(self.stats.total.average_time, 2)),
            font=self.fonts['Stats']
        )

        # Skis Labels
        self.ski_count = tk.Label(
            self,
            text=str(self.stats.ski.total_count),
            font=self.fonts['Stats']
        )
        self.ski_distance = tk.Label(
            self,
            text=str(self.stats.ski.total_distance),
            font=self.fonts['Stats']
        )
        self.ski_time = tk.Label(
            self,
            text=str(self.stats.ski.total_time),
            font=self.fonts['Stats']
        )
        self.ski_average_distance = tk.Label(
            self,
            text=str(round(self.stats.ski.average_distance, 2)),
            font=self.fonts['Stats']
        )
        self.ski_average_time = tk.Label(
            self,
            text=str(round(self.stats.ski.average_time, 2)),
            font=self.fonts['Stats']
        )

        # Runs Labels
        self.run_count = tk.Label(
            self,
            text=str(self.stats.run.total_count),
            font=self.fonts['Stats']
        )
        self.run_distance = tk.Label(
            self,
            text=str(self.stats.run.total_distance),
            font=self.fonts['Stats']
        )
        self.run_time = tk.Label(
            self,
            text=str(self.stats.run.total_time),
            font=self.fonts['Stats']
        )
        self.run_average_distance = tk.Label(
            self,
            text=str(round(self.stats.run.average_distance, 2)),
            font=self.fonts['Stats']
        )
        self.run_average_time = tk.Label(
            self,
            text=str(round(self.stats.run.average_time, 2)),
            font=self.fonts['Stats']
        )

        # Bike rides Labels
        self.bike_count = tk.Label(
            self,
            text=str(self.stats.bike.total_count),
            font=self.fonts['Stats']
        )
        self.bike_distance = tk.Label(
            self,
            text=str(self.stats.bike.total_distance),
            font=self.fonts['Stats']
        )
        self.bike_time = tk.Label(
            self,
            text=str(self.stats.bike.total_time),
            font=self.fonts['Stats']
        )
        self.bike_average_distance = tk.Label(
            self,
            text=str(round(self.stats.bike.average_distance, 2)),
            font=self.fonts['Stats']
        )
        self.bike_average_time = tk.Label(
            self,
            text=str(round(self.stats.bike.average_time, 2)),
            font=self.fonts['Stats']
        )

        # Place Labels
        self.stats_label.grid(column=1, columnspan=2, row=2, pady=15, sticky='w')
        self.averages_label.grid(column=5, row=3, sticky='w', padx=10)
        self.totals_label.grid(column=1, row=5, sticky='w')
        self.ski_label.grid(column=1, row=6, sticky='w')
        self.run_label.grid(column=1, row=7, sticky='w')
        self.bike_label.grid(column=1, row=8, sticky='w')
        self.totals_count_label.grid(column=2, row=4, sticky='w', padx=10)
        self.totals_distance_label.grid(column=3, row=4, sticky='w', padx=10)
        self.totals_time_label.grid(column=4, row=4, sticky='w', padx=10)
        self.averages_distance_label.grid(column=5, row=4, sticky='w', padx=10)
        self.averages_time_label.grid(column=6, row=4, sticky='w', padx=10)

        # All activities
        self.total_count.grid(column=2, row=5)
        self.total_distance.grid(column=3, row=5)
        self.total_time.grid(column=4, row=5)
        self.total_average_distance.grid(column=5, row=5)
        self.total_average_time.grid(column=6, row=5)

        # Skis
        self.ski_count.grid(column=2, row=6)
        self.ski_distance.grid(column=3, row=6)
        self.ski_time.grid(column=4, row=6)
        self.ski_average_distance.grid(column=5, row=6)
        self.ski_average_time.grid(column=6, row=6)

        # Runs
        self.run_count.grid(column=2, row=7)
        self.run_distance.grid(column=3, row=7)
        self.run_time.grid(column=4, row=7)
        self.run_average_distance.grid(column=5, row=7)
        self.run_average_time.grid(column=6, row=7)

        # Bike rides
        self.bike_count.grid(column=2, row=8)
        self.bike_distance.grid(column=3, row=8)
        self.bike_time.grid(column=4, row=8)
        self.bike_average_distance.grid(column=5, row=8)
        self.bike_average_time.grid(column=6, row=8)
