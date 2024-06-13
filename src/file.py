from src.assets import *
from customtkinter import *
from pathlib import Path
from PIL import Image
import fitz

class File(CTkButton):
    def __init__(self, master, file_path):
        super().__init__(master, text= self.get_title(file_path), width= 200, height= 230, compound= "top", command= self.view)
        self.path= Path(file_path)
        self.title= Path(self.path).name
        self.extension= Path(self.path).suffix
        
        #Padronizando cor para PDF/Docx/Txt
        if self.extension == ".pdf": 
            self.configure(fg_color= "#D9304F", image= IMG_PDF_ICON, hover_color="#a0233a")
            
        elif self.extension == ".docx": 
            self.configure(fg_color= "#C3D4F1", image= IMG_DOC_ICON, hover_color="#8e9ebb")
            
        elif self.extension == ".txt":
            self.configure(fg_color= "#FFFFFF", image= IMG_TXT_ICON, hover_color="#b4b4b4")

    def get_title(self, title) -> str:
        if len(Path(title).name) <30:
            return Path(title).name
        else:
            return Path(title).name[0:30] + '.'*3 

    def view(self):
        #Processando/Carregando o File
        #Criando uma janela para visualização
        imgs= self.convert_pages_to_images()
        new_master = CTkToplevel(self.master)
        new_master.title("Basic File Viewer - Modo Leitura")
        new_master.state("zoomed")

        #Frame da Janela
        #Adicionando cada pagina do file como img na interface
        frame= CTkScrollableFrame(new_master)
        frame.pack(fill="both", expand= True)
        for img in imgs:
            lbl_img = CTkLabel(frame, text=None, image=img)
            lbl_img.pack(fill=BOTH, expand=True)
            new_master.after(10, new_master.lift)

    '''
    CONVERT_PAGES_TO_IMAGES:
    -Abre determinado arquivo (para ser tratado)
    Para cada pagina do aquivo aberto:
        -carrega pagina
        -Converter pagina em um objeto Pixmap (para representar a imagem enquanto é tratada)
        -Cria uma nova imagem atraves de pixels brutos(Pixmap) 
        -Retorna uma lista com todas as paginas tratadas e convertidas em imagens
    ''' 
    def convert_pages_to_images(self) -> list:
        imgs= []
        doc = fitz.open(self.path)
        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img_ctk = CTkImage(light_image=img, size=(img.width, img.height))
            imgs.append(img_ctk)
        return imgs