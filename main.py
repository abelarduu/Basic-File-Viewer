from src import *
from customtkinter import *
from tkinter.filedialog import askopenfilename
from random import randint
from os import getcwd
from PIL import Image

class App:
    def __init__(self):
        type_extension=['file.txt', 'file.docx', 'file.pdf']
        #self.ebooks_list= list([File(FRAME_FILE, type_extension[randint(0,2)]).grid(row=l, column= c, padx=15, pady=15) for l in range(4) for c in range(9)])
        for c in range(5):
            for l in range(4):
                File(FRAME_FILE, type_extension[randint(0,2)]).grid(row=l, column= c, padx=20, pady=25)
                
        #Elementos do frame_bar
        btn_add_file= CTkButton(FRAME_BAR, text="selecionar", width= 50, height= 75, command= self.get_file)
        btn_del_file= CTkButton(FRAME_BAR, text="deletar", width= 75, height= 75, command= self.delete_file)

        #Switch Theme Dark
        self.switch_var = StringVar(value="off")
        self.switch_var.trace_add("write", lambda *args: self.toggle_theme())
        btn_theme= CTkSwitch(FRAME_BAR, text=None, width= 25, variable= self.switch_var, onvalue="on", offvalue="off")

        #Agrupando elementos do frame_bar
        #Adicionando-os na tela
        btn_bar= [btn_add_file, btn_del_file, btn_theme]
        for btn in btn_bar:
            btn.pack(padx=15, pady=10)

    def toggle_theme(self):
        if self.switch_var.get() == "on":
            MASTER.dark_theme()
        else:MASTER.clear_theme()

    def get_file(self) -> str:
        '''
        Definindo:
            -Diretorio inicial do explorador de arquivos
            -Titulo da aba
            -Tipos de arquivos aceitaveis(.pdf/.txt)
        ''' 
        #Importando Ebooks/PDF
        filedir= askopenfilename(initialdir= getcwd(),
                                title="Selecionar Arquivo",
                                filetype=(("PDF File", ".pdf"),
                                          ("Doc file",".docx"),
                                          ("Text file",".txt"),
                                          ("All File", '*')))
        return filedir

    def delete_file(self):
        dialog = CTkInputDialog(text="Nome do Arquivo:", title="Remover Arquivo")

    def run(self):
        MASTER.mainloop()

if __name__ == "__main__":
    app= App()
    app.run()
