from tkinter import Frame as tkFrame

class Frame(tkFrame):
    """Wrapper around tkFrame"""
    def __init__(self,
            master,
            width: int = 400,
            height: int = 400,
            background = "white",
            highlightbackground="white", 
            highlightthickness=0
        ):
        """Init the frame
        
        Parameters
        ----------
        master : master widget
        width : int default 400
        height : int default 400
        background : background color default white
        """
        # Check if the backgroud is transparent
        self.background = master.background if background == "transparent" else background
        super().__init__(
            master,
            width=width,
            height=height,
            background=self.background,
            highlightbackground=highlightbackground,
            highlightthickness=highlightthickness
        )