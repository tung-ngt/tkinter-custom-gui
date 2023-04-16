from tkinter.ttk import Treeview as tkTreeView, Style

class TreeView(tkTreeView):
    """Custom tree view"""
    def __init__(self, 
        master,
        columns: tuple[str],
        selectmode="browse",
        show="headings",
        yscrollcommand=None,
        style_name="Treeview"
        ):
        """Init the Tree view
        
        Parameters
        ----------
        master : master widget
        columns : (id, id,...) tuple of column identifier
        selectmode : 
        - browse (select 1 item) default
        - extended (select multiple items)
        - none (cannot select)
        show : headings, tree or tree headings
        yscrollcommand : function to control y scrolling
        style_name:
        """
        self.style_name = style_name
        super().__init__(
            master,
            columns=columns, 
            selectmode=selectmode, 
            show=show, 
            yscrollcommand=yscrollcommand,
            style=self.style_name
        )

    def config_styles(self,
            heading:dict[str, str],
            row: dict[str, str],
            selected: dict[str, str]
        ):
        """Config the table styles
        
        Parameters
        ----------
        heading : {
            background : str, 
            foreground : str,
            font : Font
        }
        row : {
            background : str,
            foreground : str,
            font : Font,
            rowheight: int
        },
        selected: {
            background : str,
            foreground : str
        }
        """
        self.style = Style(self)
        self.style.theme_use("alt")
        self.style.configure(f"{self.style_name}.Heading",
            background=heading.get("background", "white"),
            foreground=heading.get("foreground", "black"),
            font=heading.get("font", None),
            relief="raise"
        )
        self.style.configure(self.style_name,
            background=row.get("background", "white"),
            foreground=row.get("foreground", "black"),
            font=row.get("font", None),
            fieldbackground=row.get("background", "white"),
            rowheight=row.get("rowheight", 20),
        )
        self.style.map(self.style_name,
            background=[("selected", selected.get("background", "blue"))],
            foreground=[("selected", selected.get("foreground", "white"))]
        )

    def config_headings(self, configs: dict[str, dict[str, str]]):
        """Config the headings
        
        Parameters
        ----------
        configs : {
            columnid : {
                text : str,
                anchor : str (text align)
            }
        }
        """
        for columnid, config in list(configs.items()):
            self.heading(
                columnid, 
                text=config.get("text", ""), 
                anchor=config.get("anchor", "center")
            )

    def config_columns(self, configs: dict[str, dict[str, str]]):
        """Config the columns
        
        Parameters
        ----------
        configs : {
            columnid : {
                width : initial width (int)
                minwidth : minimum width (int)
                anchor : str (text align),
                stretch : bool
            }
        }
        """

        for columnid, config in list(configs.items()):
            if "width" in config.keys():
                self.column(
                    columnid,
                    width=config.get("width"),
                    minwidth=config.get("width", 30),
                    stretch=config.get("stretch", True),
                    anchor=config.get("anchor", "w"),
                )
            else:
                self.column(
                    columnid,
                    minwidth=config.get("width", 30),
                    stretch=config.get("stretch", True),
                    anchor=config.get("anchor", "w"),
                )