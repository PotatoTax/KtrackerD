import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import main
import SheetTools


class Authorization(tk.Tk):

    def __init__(self, admin_key):

        # Initializes and names the window
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, string="Authorizer")

        # Used for debugging, skips login process and enters as user 'Admin'
        if admin_key == '10267':
            main.currentUser = 'Admin'
            self.destroy()
            main.boot_app()
            quit()

        # Creates container for pages
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Creates instances of LoginScreen and SignUpScreen
        for F in (LoginScreen, SignUpScreen):
            frame = F(self.container, self)

            self.frames[F] = frame

            # Places them in the window
            frame.grid(column=0, row=0, sticky="nsew")

        # Opens the Login screen
        self.switch_frame(1)

    def switch_frame(self, page):  # Manages switching pages
        # If the page is 1, open login, else open signup
        if page == 1:
            frame = LoginScreen(self.container, self)
        else:
            frame = SignUpScreen(self.container, self)
        # Selects the username entry box and sets up the page
        frame.username_input.focus()
        frame.grid(column=0, row=0, sticky="nsew")
        frame.tkraise()
        tk.Tk.wm_title(
            self,
            string=("KTracker | " + frame.name)
        )


class LoginScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Fonts used in this page
        self.fonts = {
            'TitleText': ('Roboto', '25', 'bold')
        }

        self.configure(bg='#f5f5fa')
        self.controller = controller
        self.name = 'Login'

        # Initialize Widgets
        self.login_label = tk.Label(self, text='Login', font=self.fonts['TitleText'], bg='#f5f5fa')
        self.username_label = tk.Label(self, text='Username : ', bg='#f5f5fa')
        self.password_label = tk.Label(self, text='Password : ', bg='#f5f5fa')

        self.username_input = tk.Entry(self)
        self.password_input = tk.Entry(self, show="\u2022")

        self.submit = ttk.Button(self, text='Submit', command=lambda: self.login())
        self.signup = ttk.Button(self, text='Sign Up', command=lambda: self.switch_mode())

        # Place Widgets
        self.login_label.grid(column=0, row=0, padx=10, pady=10)
        self.username_label.grid(column=0, row=1)
        self.password_label.grid(column=0, row=2)

        self.username_input.grid(column=1, row=1)
        self.password_input.grid(column=1, row=2)

        self.submit.grid(column=0, row=3, padx=5, pady=5)
        self.signup.grid(column=0, row=4, padx=5, pady=5)

    def login(self):
        username = self.username_input.get()
        password = self.password_input.get()

        if not username or not password:
            return False

        try:
            SheetTools.get_user_data(username)
            if SheetTools.get_password(username) == password:
                main.currentUser = username
                self.controller.destroy()
                main.boot_app()
                return True
            else:
                tk.messagebox.showerror(
                    'Error',
                    'Sorry, unrecognized username or password.'
                )
                return False
        except ValueError:
            tk.messagebox.showerror(
                'Error',
                'Sorry, unrecognized username or password.'
            )
            return False

    def switch_mode(self):
        self.controller.switch_frame(2)
        self.destroy()


class SignUpScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Fonts used in this page
        self.fonts = {
            'TitleText': ('Roboto', '25', 'bold')
        }

        self.configure(bg='#f5f5fa')
        self.controller = controller
        self.name = 'Sign Up'

        # Declare Widgets
        self.sign_up_label = tk.Label(self, text='Sign Up', font=self.fonts['TitleText'], bg='#f5f5fa')
        self.username_label = tk.Label(self, text='Username : ', bg='#f5f5fa')
        self.password1_label = tk.Label(self, text='Password : ', bg='#f5f5fa')
        self.password2_label = tk.Label(self, text='Confirm : ', bg='#f5f5fa')

        self.username_input = tk.Entry(self)
        self.password1_input = tk.Entry(self, show="\u2022")
        self.password2_input = tk.Entry(self, show="\u2022")

        self.submit = ttk.Button(self, text='Submit', command=lambda: self.add_user())
        self.login = ttk.Button(self, text='Login', command=lambda: self.switch_mode())

        # Arrange Widgets
        self.sign_up_label.grid(column=0, row=0, padx=10, pady=10)
        self.username_label.grid(column=0, row=1)
        self.password1_label.grid(column=0, row=2)
        self.password2_label.grid(column=0, row=3)

        self.username_input.grid(column=1, row=1)
        self.password1_input.grid(column=1, row=2)
        self.password2_input.grid(column=1, row=3)

        self.submit.grid(column=0, row=4, padx=5, pady=5)
        self.login.grid(column=0, row=5, padx=5, pady=5)

    def add_user(self):
        # Retrieves username and password from inputs
        username = self.username_input.get()
        password1 = self.password1_input.get()
        password2 = self.password2_input.get()

        # Ensures there has been input
        if not username or not password1 or not password2:
            return False

        # Returns 1 if user exists, 2 if successful, 3 if passwords don't match
        result = SheetTools.add_user(username, password1, password2)

        if result == 1:
            # Notifies user that user already exists
            tk.messagebox.showerror(
                'Error',
                'Sorry, user already exists.'
            )
            return False

        elif result == 2:
            # Destroys the window and starts the main app
            self.controller.destroy()
            main.boot_app()
            return True

        elif result == 3:
            # Notifies the user that the passwords don't match
            tk.messagebox.showerror(
                'Error',
                'Sorry, passwords don\'t match'
            )
            return False

    def switch_mode(self):
        self.controller.switch_frame(1)
        self.destroy()
