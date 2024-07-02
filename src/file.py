from customtkinter import CTkButton, CTkLabel, CTkToplevel, CTkImage, CTkScrollableFrame
from pathlib import Path
from PIL import Image
import fitz
from src.assets import *

class File(CTkButton):
    def __init__(self, master, file_path):
        super().__init__(master, text=self.get_title(file_path), width=200, height=230, compound="top", command=self.view)
        self.path = Path(file_path)
        self.title = Path(self.path).name
        self.extension = Path(self.path).suffix
        
        # Define a cor e o ícone baseado na extensão do arquivo
        if self.extension == ".pdf": 
            self.configure(fg_color="#D9304F", image=IMG_PDF_ICON, hover_color="#a0233a")
        elif self.extension == ".docx": 
            self.configure(fg_color="#C3D4F1", image=IMG_DOC_ICON, hover_color="#8e9ebb")
        elif self.extension == ".txt":
            self.configure(fg_color="#FFFFFF", image=IMG_TXT_ICON, hover_color="#b4b4b4")

    def get_title(self, title) -> str:
        """Retorna o título do arquivo formatado para exibição na interface."""
        if len(Path(title).name) < 28:
            return Path(title).name.lower()
        else:
            return Path(title).name[0:28].lower() + '...' 

    def view(self):
        """Abre uma nova janela para visualização do arquivo."""
        imgs = self.convert_pages_to_images()
        new_master = CTkToplevel(self.master)
        new_master.title("Basic File Viewer - Modo Leitura")
        new_master.state("zoomed")

        # Frame da Janela
        frame = CTkScrollableFrame(new_master)
        frame.pack(fill="both", expand=True)
        
        # Adiciona cada página do arquivo como imagem na interface
        for img in imgs:
            lbl_img = CTkLabel(frame, text=None, image=img)
            lbl_img.pack(fill="both", expand=True)
            new_master.after(10, new_master.lift)

    def convert_pages_to_images(self) -> list:
        """Converte as páginas de um arquivo em imagens para visualização."""
        imgs = []
        if self.path.exists():
            doc = fitz.open(self.path)
            for page_number in range(len(doc)):
                page = doc.load_page(page_number)
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                img_ctk = CTkImage(light_image=img, size=(img.width, img.height))
                imgs.append(img_ctk)
            return imgs
        else:
            self.destroy()  # Destruir o widget se o arquivo não existir
