from src import *
from tkinter.filedialog import askopenfilename

class App:
    def __init__(self):
        """Inicializa a aplicação e define os botões da interface."""
        # Logo do app
        icon = CTkLabel(FRAME_READER, image=IMG_LOGO, text=None)
        icon.pack(pady=10)
        
        # Elementos do frame_bar
        btn_add_file = CTkButton(FRAME_BAR, image=BTN_IMPORT_ICON, text=None, width=50, height=75, command=self.add_file)
        btn_del_file = CTkButton(FRAME_BAR, image=BTN_DELETE_ICON, text=None, width=75, height=75, command=self.delete_file)
        lbl_img_moon = CTkLabel(FRAME_BAR, image=IMG_MOON_ICON, text=None)

        # Switch Theme Dark
        self.switch_var = StringVar(value="off")
        self.switch_var.trace_add("write", lambda *args: self.toggle_theme())
        btn_theme = CTkSwitch(FRAME_BAR, text=None, width=25, variable=self.switch_var, onvalue="on", offvalue="off")
        
        # Agrupando elementos do frame_bar e adicionando-os na tela
        btn_bar = [btn_add_file, btn_del_file, lbl_img_moon, btn_theme]
        for btn in btn_bar:
            btn.pack(padx=15, pady=10)

    def toggle_theme(self):
        """Ativa ou desativa o modo theme Dark."""
        if self.switch_var.get() == "on":
            MASTER.dark_theme()
        else:
            MASTER.clear_theme()
    
    def draw_files(self):
        """Desenha os arquivos na interface."""
        path_index = 2
        max_columns = 5
        files_list = DB.get_datas()
        
        # Iteração com a lista de Files
        for index, file in enumerate(files_list):
            row = index // max_columns
            column = index % max_columns
            new_file = File(FRAME_FILE, file[path_index])
            new_file.grid(row=row, column=column, padx=20, pady=25)

    def add_file(self):
        """Adiciona um novo arquivo à lista."""
        # Importando Ebooks/PDF
        '''Definindo:
            - Diretório inicial do explorador de arquivos
            - Título da aba
            - Tipos de arquivos aceitáveis (.pdf/ .docx/ .txt)''' 
        filedir = askopenfilename(initialdir=getcwd(),
                                  title="Selecionar Arquivo",
                                  filetype=(("PDF File", ".pdf"),
                                            ("Doc file", ".docx"),
                                            ("Text file", ".txt"),
                                            ("All File", '*')))
        if not filedir == "":
            # Criando um novo "File" 
            # Adicionando no Banco de Dados
            new_file = File(FRAME_FILE, filedir)
            DB.add_data((new_file.title, str(new_file.path), new_file.extension))
            MASTER.after(10, self.draw_files)
            
    def delete_file(self):
        """Remove um arquivo da lista."""
        dialog = CTkInputDialog(text="Nome do Arquivo:", title="Remover Arquivo")
        title_file = dialog.get_input()
        DB.delete_data(title_file)
        MASTER.after(10, self.draw_files)
 
    def run(self):
        """Inicia a aplicação e mantém a interface em execução."""
        MASTER.after(10, self.draw_files)
        MASTER.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()