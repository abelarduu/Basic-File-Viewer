from src.window import Window
from src.assets import IMG_PDF_ICON, IMG_DOC_ICON, IMG_TXT_ICON
from customtkinter import CTkButton, CTkToplevel

class File(CTkButton):
    def __init__(self, master, name):
        super().__init__(master, text= name, width= 200, height= 230, compound= "top", command= self.view)
        self.file_extension= name[name.find('.')+1:]
        if self.file_extension == "pdf": self.configure(fg_color= "#D9304F", image= IMG_PDF_ICON, hover_color="#a0233a")
        if self.file_extension == "docx": self.configure(fg_color= "#C3D4F1", image= IMG_DOC_ICON, hover_color="#8e9ebb")
        if self.file_extension == "txt": self.configure(fg_color= "#FFFFFF", image= IMG_TXT_ICON, hover_color="#b4b4b4")

    def view(self):
        new_master= CTkToplevel()
        new_master.title("Basic File Viewer - Modo Leitura")
        new_master.state("zoomed")
        #abrir o file nessa janela

    def delete(self):
        pass