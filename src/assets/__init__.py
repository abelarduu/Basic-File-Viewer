from customtkinter import CTkImage
from pathlib import Path
from PIL import Image

PATH= Path(__file__).parent

#IMGS
IMG_LOGO = CTkImage(light_image=Image.open(PATH / "images/logo.png"), size=(356, 100))
IMG_TXT_ICON = CTkImage(light_image=Image.open(PATH / "images/txt_icon.png"), size=(120, 170))
IMG_DOC_ICON = CTkImage(light_image=Image.open(PATH / "images/docx_icon.png"), size=(120, 170))
IMG_PDF_ICON = CTkImage(light_image=Image.open(PATH / "images/pdf_icon.png"), size=(120, 170))
BTN_IMPORT_ICON= CTkImage(light_image=Image.open(PATH / "images/btn_import_icon.png"), size=(64, 90))
BTN_DELETE_ICON= CTkImage(light_image=Image.open(PATH / "images/btn_delete_icon.png"), size=(64, 90))
IMG_MOON_ICON= CTkImage(light_image=Image.open(PATH / "images/moon_icon.png"), size=(32, 36))
