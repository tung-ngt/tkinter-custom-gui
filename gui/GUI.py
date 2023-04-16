from tkinter import Tk, NSEW, PhotoImage
from tkinter.font import Font

from .Screen import Screen
from .Navbar import Navbar
from .Frame import Frame

import os
from ctypes import windll

class GUI(Tk):
    """GUI app class"""
    def __init__(self, 
            title, 
            geometry="800x600", 
            resizable=(True, True),
            fullscreen=False,
            min_size=(0,0), 
            icon=None,
            on_close_fun=None
        ):
        """Init gui
        
        Parameters
        ----------
        title : title of the window
        geometry : initial geometry of the window string "{width}x{height}" default "800x600"
        resizable : if the window can change size (width, height) default (False, False)
        fullscreen : bool if the app is fullscreen (default False)
        min_size : (width: int, height: int)
        icon : path to icon default None
        fonts : fonts that is used in the app
        on_close_fun : function to run when x button is clicked
        """
        # Fix blurry problem 
        windll.shcore.SetProcessDpiAwareness(1)
        
        super().__init__()

        # Setup custom function when close
        self.on_close_fun = on_close_fun
        if self.on_close_fun != None:
            self.protocol("WM_DELETE_WINDOW", self.on_close_fun)

        # Set title
        self.title(title)   

        # Set screen dimensions     
        self.geometry(geometry)
        if fullscreen:
            self.state("zoomed")
        self.resizable(resizable[0], resizable[1])
        self.minsize(min_size[0], min_size[1])
        
        # Set window icon
        if os.path.isfile(icon):
            self.iconphoto(True, PhotoImage(file=icon))

        # Setup screen for navigation
        self.__screens: dict[str, Screen] = {}
        self.__current_screen: str = None
        
        # Specify navbar and screen grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=150)
        self.grid_columnconfigure(1, weight=9)

        self.screens_frame = Frame(self)
        self.screens_frame.grid(row=0, column=1, sticky="nsew")
        self.screens_frame.pack_propagate(False)

    def init_navbar(self, navbar: Navbar):
        """Add navbar and place it in root window"""    
        self.navbar = navbar
        self.navbar.grid(row=0, column=0, sticky=NSEW)

    def add_screen(self, screen_name: str, screen: Screen):
        """Add screen to the app
        
        Parameters
        ----------
        screen_name : name of the screen,
        screen : the screen
        """
        self.__screens[screen_name] = screen

    def change_screen(self, screen_name: str):
        """Change screen to a specified screen"""
        self.hide_screen(self.__current_screen)
        self.show_screen(screen_name)

    def hide_screen(self, screen_name: str):
        """Hide a screen"""
        self.__screens[screen_name].pack_forget()
    
    def show_screen(self, screen_name: str):
        """Show a screen"""
        self.__screens[screen_name].pack(fill="both", expand=True)
        self.__current_screen = screen_name