from customtkinter import CTkImage
from pathlib import Path
from PIL import Image

PATH= Path(__file__).parent

#IMGS
IMG_PDF_ICON = CTkImage(light_image=Image.open(PATH / "images/pdf_icon.png"), size=(120, 170))
IMG_DOC_ICON = CTkImage(light_image=Image.open(PATH / "images/docx_icon.png"), size=(120, 170))
IMG_TXT_ICON = CTkImage(light_image=Image.open(PATH / "images/txt_icon.png"), size=(120, 170))
