from customtkinter import CTk, set_appearance_mode
from src.assets import PATH

class Window(CTk):
    def __init__(self, w:int, h:int, title:str, resizable:bool):
        super().__init__()
        self.title(title)
        self.minsize(w, h)
        self.state("zoomed")
        self.resizable(resizable, resizable)
        self.iconbitmap(PATH / 'images/icon.ico') 
        set_appearance_mode("light")
        
        self.columnconfigure(5, weight=5)
        self.rowconfigure(2, weight=2)

    def dark_theme(self):
        set_appearance_mode("dark")

    def clear_theme(self):
        set_appearance_mode("light")