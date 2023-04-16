from tkinter import Button as tkButton, PhotoImage
from tkinter.font import Font

class Button(tkButton):
    """Wrapper around tkButton"""
    def __init__(self, 
            master, 
            command,
            text,
            width=None, height=None,
            background="white", foreground="black",
            activebackground="grey", activeforeground="black",
            borderwidth=0, 
            image: PhotoImage or str=None,
            font: Font=None,
            compound: str=None,
            hover_background:str = None,
            hover_foreground:str = None
        ):
        """Init the button
        
        Parameters
        ----------
        master : master widget
        command : function to run when press
        width : int
        height : int
        background
        foreground
        activebackground
        activeforeground
        borderwidth : default 0
        image : label image path (default None)
        font : a tk font type default None
        compound : image and text relative position default None
        hover_background
        hover_foreground
        """
        # Check if the backgroud is transparent
        if background == "transparent":
            background = master.background

        # Check if the label have image
        self.label_image: PhotoImage = None
        if image != None:
            if isinstance(image, str):
                self.label_image = PhotoImage(file=image)
            else:
                self.label_image = image

        super().__init__(
            master, 
            activebackground=activebackground, 
            activeforeground=activeforeground,
            background=background,
            foreground=foreground,
            borderwidth=borderwidth,
            command=command,
            font=font,
            text=text,
            width=width,
            height=height,
            cursor="hand2",
            image=self.label_image,
            compound=compound
        )

        # Bind hover event
        self.default_background = background
        self.default_foreground = foreground
        self.hover_background =  hover_background if hover_background != None else activebackground
        self.hover_foreground =  hover_foreground if hover_foreground != None else activeforeground
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        """Change background on hover"""
        self["background"] = self.hover_background
        self["foreground"] = self.hover_foreground
    
    def on_leave(self, event):
        """Reset background on leave"""
        self["background"] = self.default_background
        self["foreground"] = self.default_foreground