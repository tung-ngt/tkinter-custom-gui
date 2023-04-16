from tkinter.font import Font

class Typography:
    """Typography is use to store configurations about fonts, types, ..."""
    def __init__(self, 
        settings: dict[str, dict[str: int or str]] or None = None
        ):
        """Init typography
        
        Parameters
        ----------
        settings : {font_name: {family: str, size: int}}
        """
        self.root = None
        self.fonts: dict[str, dict[str, Font]] = {}

        if settings == None:
            self.settings = \
            {
                "paragraph": {
                    "family": "Times New Roman",
                    "size": 16,
                },
                "heading1": {
                    "family": "Times New Roman",
                    "size": 48
                },
                "heading2": {
                    "family": "Times New Roman",
                    "size": 32
                },
                "heading3": {
                    "family": "Times New Roman",
                    "size": 24,
                },
            }
        else:
            self.settings = settings
    

    def init_fonts(self, master):
        """Initialize fonts with settings
        
        Parameters:
        master : master widget
        """

        # Set root to master widget
        self.root = master
        self.create_variations(self.settings)
        
            
    def create_variations(self, settings: dict[str, dict[str, str or int]]):
        """Create font and their variation and return it
        
        Parameters
        ----------
        settings : {font_name: {family: str, size: int}}
        """
        fonts = {}
        for font_name, font_settings in list(settings.items()):
            font_variations = {}
            new_font = Font(self.root, family=font_settings["family"], size=font_settings["size"])

            for w in ["normal", "bold"]:
                for s in ["roman", "italic"]:
                    v = new_font.copy()
                    v.config(weight=w, slant=s)
                    font_variations[w+s] = v

            fonts[font_name] = font_variations
        
        self.fonts = fonts

    def get_font_names(self):
        return self.fonts.keys()

    def get_font(self, font_name, bold=False, italic=False):
        """Return the fonts
        
        Parameters
        ----------
        font_name : font_name included
        bold : default False
        italic : default False
        """
        # Check if the font exist
        if font_name not in self.get_font_names():
            raise Exception("Invalid font")

        variation = ("bold" if bold else "normal") + ("italic" if italic else "roman")
        return self.fonts[font_name][variation]