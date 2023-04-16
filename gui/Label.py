from tkinter import Label as tkLabel, PhotoImage
from tkinter.font import Font

class Label(tkLabel):
    """Custom Label"""
    def __init__(self,
            master,
            text: str="",
            foreground="black",
            background="white",
            font: Font=None,
            image: PhotoImage or str=None,
            cursor: str=None,
            compound: str=None,
            justify: str = "center"
        ):
        """Init the label
        
        Parameters
        ----------
        master : master widget,
        text : str text
        foreground : text color (default black)
        background : background color (default white) specify transparent for transparent 
        font : a tk font (default None)
        image : label image path (default None)
        cursor : the pointer cursor when hover default None
        compound : image and text relative position default None
        justify : text justify
        """
        # Check if the backgroud is transparent
        background = master.background if background == "transparent" else background
        
        # Check if the label have imgage
        self.label_image: PhotoImage = None
        if image != None:
            if isinstance(image, str):
                self.label_image = PhotoImage(file=image)
            else:
                self.label_image = image
        
        super().__init__(master,
            text=text,
            background=background,
            foreground=foreground,
            font=font,
            cursor=cursor,
            image=self.label_image,
            compound=compound,
            justify=justify
        )