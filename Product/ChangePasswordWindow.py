import tkinter as tk
from tkinter import messagebox

import SheetTools
import main


class ChangePasswordWindow:

    def __init__(self):

        # Create and name window
        self.Frame = tk.Tk()
        tk.Tk.wm_title(
            self.Frame,
            string='KTracker | Change Password'
        )

        # Fonts used in window
        self.fonts = {
            'TitleText': ('Roboto', '25', 'bold')
        }

        # Initialize Widgets
        self.change_pass_label = tk.Label(self.Frame, text='Change Password', font=self.fonts['TitleText'])
        self.old_pass_label = tk.Label(self.Frame, text='Old Password')
        self.new_pass1_label = tk.Label(self.Frame, text='New Password')
        self.new_pass2_label = tk.Label(self.Frame, text='Confirm')

        self.old_pass_input = tk.Entry(self.Frame, show='\u2022')
        self.new_pass1_input = tk.Entry(self.Frame, show='\u2022')
        self.new_pass2_input = tk.Entry(self.Frame, show='\u2022')

        self.submit = tk.Button(self.Frame, text='Submit', command=self.change_pass)

        # Place Widgets
        self.old_pass_input.grid(column=1, row=1)
        self.new_pass1_input.grid(column=1, row=2)
        self.new_pass2_input.grid(column=1, row=3)

        self.change_pass_label.grid(column=0, columnspan=2, row=0)
        self.old_pass_label.grid(column=0, row=1)
        self.new_pass1_label.grid(column=0, row=2)
        self.new_pass2_label.grid(column=0, row=3)

        self.submit.grid(column=1, row=4)

    def change_pass(self):
        # Retrieve password inputs
        old_pass = self.old_pass_input.get()
        new_pass1 = self.new_pass1_input.get()
        new_pass2 = self.new_pass2_input.get()

        # Check if the old password is correct
        if not SheetTools.get_password(main.currentUser) == old_pass:
            tk.messagebox.showerror('Error', 'Current password is incorrect.')
            return 1

        # If the new passwords match, update the document and close the window
        if new_pass1 == new_pass2:
            sheet = SheetTools.get_worksheet(main.currentUser)
            sheet.update_acell('A1', new_pass1)
            tk.messagebox.showinfo('Done', 'Password changed successfully')
            self.Frame.destroy()
        else:
            tk.messagebox.showerror('Error', 'Passwords do not match.')
            return 1
