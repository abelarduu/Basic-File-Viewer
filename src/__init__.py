from src.file import File
from src.window import Window
from src.database import Database
from customtkinter import *

DB= Database()
MASTER= Window(870,530,"Basic File Viewer", True)
#FRAMES
#READER
READER= CTkFrame(MASTER,height= 100, fg_color= "#3264A6", corner_radius=0)
READER.grid(row=1, column= 1, columnspan=5, sticky='nsew')
#FRAME DE BARRA
FRAME_BAR= CTkFrame(MASTER, width= 100, fg_color= "#205191", corner_radius=0)
FRAME_BAR.grid(row=2, column= 1, rowspan=3, sticky='ns')
#FRAME DE ARQUIVOS
FRAME_FILE= CTkScrollableFrame(MASTER, width= 500)
FRAME_FILE.grid(row=2, column= 3, columnspan=5, sticky='nsew', padx=15, pady=15)