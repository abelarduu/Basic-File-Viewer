from src import *
from src.assets import *
from customtkinter import *
from tkinter.filedialog import askopenfilename
from os import getcwd

class App:
    def __init__(self):
        self.file_list= tuple()
        #Elementos do frame_bar
        btn_add_file= CTkButton(FRAME_BAR, image= BTN_IMPORT_ICON, text=None, width= 50, height= 75, command= self.add_file)
        btn_del_file= CTkButton(FRAME_BAR, image= BTN_DELETE_ICON, text=None, width= 75, height= 75, command= self.delete_file)
        lbl_img_moon= CTkLabel(FRAME_BAR, image= IMG_MOON_ICON, text= None)

        #Switch Theme Dark
        self.switch_var = StringVar(value="off")
        self.switch_var.trace_add("write", lambda *args: self.toggle_theme())
        btn_theme= CTkSwitch(FRAME_BAR, text=None, width= 25, variable= self.switch_var, onvalue="on", offvalue="off")
        #Agrupando elementos do frame_bar e Adicionando-os na tela
        btn_bar= [btn_add_file, btn_del_file,lbl_img_moon, btn_theme]
        for btn in btn_bar:
            btn.pack(padx=15, pady=10)

    def toggle_theme(self):
        if self.switch_var.get() == "on":
            MASTER.dark_theme()
        else:MASTER.clear_theme()
    
    def draw_files(self):
        index=0
        files_list= DB.get_datas()
        for line in range(len(files_list)):
            for column in range(5):
                try:
                    new_file= File(FRAME_FILE, files_list[index][1])
                    new_file.grid(row=line, column= column, padx=20, pady=25)
                    index+=1
                except IndexError: pass

    def add_file(self):
        #Importando Ebooks/PDF
        '''Definindo:
            -Diretorio inicial do explorador de arquivos
            -Titulo da aba
            -Tipos de arquivos aceitaveis(.pdf/ .docx/ .txt)''' 
        filedir= askopenfilename(initialdir= getcwd(),
                                title="Selecionar Arquivo",
                                filetype=(("PDF File", ".pdf"),
                                          ("Doc file",".docx"),
                                          ("Text file",".txt"),
                                          ("All File", '*')))
        if not filedir == "":
            #Criando um novo "File" 
            #Adicionando no Banco de Dados
            new_file= File(FRAME_FILE, filedir)
            DB.add_data((new_file.title , str(new_file.path), new_file.extension))
            MASTER.after(10, self.draw_files)

    def delete_file(self):
        dialog = CTkInputDialog(text="Nome do Arquivo:", title="Remover Arquivo")
        title_file= dialog.get_input()
        DB.delete_data(title_file)
        MASTER.after(10, self.draw_files)
 
    def run(self):
        MASTER.after(10, self.draw_files)
        MASTER.mainloop()

if __name__ == "__main__":
    app= App()
    app.run()