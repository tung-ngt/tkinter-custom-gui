from .Frame import Frame
from .Label import Label
from tkinter import PhotoImage
from tkinter.font import Font
from .SubScreen import SubScreen
from .Button import Button

class Screen(Frame):
    """Represent a screen in the gui"""
    def __init__(self, 
            master,
            background="#ffffff",
            title: str = "Title bar",
            title_bar_foreground="#000000",
            title_font: Font = None,
            title_image: PhotoImage or str = None,
            back_font: Font = None
        ):
        """Init the screen
        
        Parameters
        ----------
        master : master widget
        background : background color
        title : screen title
        title_bar_background : the color of the title bar
        title_bar_foreground : the color of title text
        title_font : font of the title
        """
        super().__init__(master, background=background)
        # Make the screen take up the whole available space
        # instead of skrinking to children widgets
        self.grid_propagate(False)
        # self.pack_propagate(False)

        self.main_frame = Frame(self, background=background)
        self.main_frame.pack_propagate(False)
        self.main_frame.grid_propagate(False)

        # Config the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1, minsize=40)
        self.grid_rowconfigure(1, weight=9)

        # Create the screen title bar

        self.title = title
        self.title_image = title_image
        self.title_bar_foreground=title_bar_foreground
        self.title_font = title_font
        self.back_font = back_font
        self.__create_screen_title_bar(self.title, self.title_bar_foreground)

        self.main_frame.grid(row=1, column=0, sticky="nsew")

        # Init variable for sub-navigation
        self.__subscreens: dict[str, SubScreen] = {}
        self.__navigation_stack: list[str] = []

    def add_subscreen(self, subscreen_name: str, subscreen: SubScreen):
        """Add a subcreen to the screen
        
        Parameters
        ----------
        subscreen_name : name of the subscreen
        subscreen : the subscreen to add
        """
        self.__subscreens[subscreen_name] = subscreen

    def __create_screen_title_bar(self,
            title_text: str,
            title_bar_foreground,
        ):
        """Creates the screen title bar"""
        self.title_bar = Frame(self, background=self.background)
        self.title_bar.grid(row=0, column=0, sticky="ew")
        self.title_bar.back_button = Button(self.title_bar,
            self.navigate_back, 
            "Back",
            background="transparent",
            image="./images/back.png", 
            compound="left",
            font=self.back_font
        )

        self.title_label = Label(self.title_bar,
            text=title_text,
            background="transparent",
            foreground=title_bar_foreground,
            font=self.title_font,
            image=self.title_image,
            compound="left" if self.title_image != None else None
        )

        self.title_label.pack()

    def __update_screen_title_bar(self,
            title_text: str=None,
            title_bar_foreground: str=None,
            title_image: str=None,  
        ):
        """Update the screen title bar
        
        Parameters
        title_text
        title_bar_forground
        title_image

        leave None for remaning the same
        """
        # Add back icon
        if len(self.__navigation_stack) > 1:
            self.title_bar.back_button.place(x=20, rely=0.5, anchor="w")
        else:
            self.title_bar.back_button.place_forget()
        # Update the title label
        title_text = title_text if title_text != None else self.title
        title_bar_foreground = title_bar_foreground if title_bar_foreground != None else self.title_bar_foreground
        title_image = title_image if title_image != None else self.title_image
        self.title_label.config(text=title_text, image=title_image, foreground=title_bar_foreground)

    # Handle sub-navigation
    def hide_subscreen(self, subscreen_name: str):
        self.__subscreens[subscreen_name].pack_forget()

    def show_subscreen(self, subscreen_name: str, props=None, back: bool=False):
        """Show a subscreen
        
        Parameters
        ----------
        props : infomation pass to render function
        back : bool if the subscreen is navigated to using back button
        """
        # Only re-render the subscreen if push onto the stack to retain state
        if not back:
            self.__subscreens[subscreen_name].render(props)

        # Repack the subscreen
        self.__subscreens[subscreen_name].pack(fill="both", expand=True)

    def navigate_subscreen(self, subscreen_name: str, props=None):
        """Navigate to a subscreen"""

        # Check if the navigation stack is empty
        if len(self.__navigation_stack) >= 1:
            self.hide_subscreen(self.__navigation_stack[-1])

        self.show_subscreen(subscreen_name, props)
        self.__navigation_stack.append(subscreen_name)

        # Update the title bar
        new_screen = self.__subscreens[subscreen_name]
        self.__update_screen_title_bar(
            new_screen.title, 
            new_screen.title_bar_foreground, 
            new_screen.title_image
        )
    
    def navigate_back(self, props = None):
        if len(self.__navigation_stack) == 1:
            return
        self.hide_subscreen(self.__navigation_stack.pop())
        self.show_subscreen(self.__navigation_stack[-1], props, back=True)

        # Update the title bar
        new_screen = self.__subscreens[self.__navigation_stack[-1]]
        self.__update_screen_title_bar(
            new_screen.title, 
            new_screen.title_bar_foreground, 
            new_screen.title_image
        )
