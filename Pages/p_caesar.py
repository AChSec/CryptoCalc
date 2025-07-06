import customtkinter as ctk
from functions  import caesar_substitution
from texts      import caesar_info, caesar_output_info
from utils      import insert_info


def caesar(ctx):		
    def run():
        try:
            result = caesar_substitution(entry_text.get(), int(entry_key.get()))
            ctx.output_label.configure(text=result + "\n\n" + caesar_output_info, font=("Roboto", 14))
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
    
    entry_text = ctk.CTkEntry(ctx.content, placeholder_text="Texteingabe")
    entry_key = ctk.CTkEntry(ctx.content, placeholder_text="Schlüssel")
    entry_text.pack(pady=5, padx=5)
    entry_key.pack(pady=5, padx=5)
    
    image = ctx.images.get("caesar")
    if image:
        ctk.CTkLabel(ctx.content, image=image, text="", 
               width=200, compound="left").pack(padx=3, pady=(10,5), fill="both")	

    ctk.CTkButton(ctx.content, text="Berechnen", command=run).pack(pady=10)

    insert_info(ctx.info_box, "Info", caesar_info)

