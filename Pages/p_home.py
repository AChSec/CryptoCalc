import customtkinter as ctk
from texts  import introduction
from utils  import insert_info

def home(ctx): 
    
    image = ctx.images.get("logo")
    if image:						
        ctk.CTkLabel(ctx.content, image=image, text="", 
                     justify="left").pack(padx=5, pady=(0, 15), side="left")
    
    ctk.CTkLabel(ctx.content, text="Kryptographie Rechner", 
                 font=("Roboto", 14, "bold")).pack(padx=7, pady=(5, 40), side="left")
    
    insert_info(ctx.info_box, "Einführung in die Kryptographie und Kryptoanalyse", introduction)