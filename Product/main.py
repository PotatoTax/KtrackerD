import tkinter as tk

import AddActivityScreen
import HomeScreen
import ProfileScreen
import auth

currentUser = None


class KTrackerApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        # Initializes and sets up window
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, string="KTracker")
        self.geometry('1440x380')

        # Sets up container (all pages are placed in this frame)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Creates menubar, adds a button for each page
        self.menubar = tk.Menu(self.container)
        self.menubar.add_command(label="Exit", command=quit)
        self.menubar.add_command(
            label="Home",
            command=lambda: self.switch_frame(HomeScreen.HomeScreen)
        )
        self.menubar.add_command(
            label="Profile",
            command=lambda: self.switch_frame(ProfileScreen.ProfileScreen)
        )
        self.menubar.add_command(
            label="Add Activity",
            command=lambda: self.switch_frame(AddActivityScreen.AddActivityScreen)
        )
        tk.Tk.config(self, menu=self.menubar)

        self.frames = {}

        self.pages = [  # List of all page objects
            HomeScreen.HomeScreen,
            ProfileScreen.ProfileScreen,
            AddActivityScreen.AddActivityScreen
        ]

        # Creates all pages, places them in container frame
        for F in self.pages:
            frame = F(self.container, self)
            frame.grid(column=0, row=0, sticky='nsew')

        # Opens the home page
        self.switch_frame(HomeScreen.HomeScreen)

    def switch_frame(self, f):

        # If the frame doesn't exist, create it
        if f in self.frames:
            frame = self.frames[f]
        else:
            frame = f(self.container, self)
            self.frames[f] = frame
            frame.grid(column=0, row=0, sticky='nsew')

        # Bring the frame to the front and name window
        frame.tkraise()
        tk.Tk.wm_title(
            self,
            string=("KTracker | " + frame.name)
        )


def boot_app():
    # Called by the Login or SignUp methods once the user is authorized
    # Creates an instance of KTrackerApp
    app = KTrackerApp()
    app.mainloop()


if __name__ == "__main__":
    # Creates an instance of Authorization
    auth = auth.Authorization('')
    auth.geometry("360x360")
    auth.mainloop()
