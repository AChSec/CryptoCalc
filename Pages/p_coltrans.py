import customtkinter as ctk
from texts      import transposition
from functions  import columnar_transposition
from utils      import insert_info


def col_trans(ctx):
    def run():
        try:
            result = columnar_transposition(entry_text.get())
            ctx.output_label.configure(text=f"{result}", font=("Roboto", 14), justify="center")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
    
    image = ctx.images.get("scytale")
    if image:
        ctk.CTkLabel(ctx.content, image=image, text="").pack(pady=0, anchor="n")
    
    entry_text = ctk.CTkEntry(ctx.content, placeholder_text="Geheimtext:", width=250)
    entry_text.pack(pady=5)
    
    ctk.CTkButton(ctx.content, text="Berechnen", command=run).pack(pady=10)
    
    insert_info(ctx.info_box, "Info", transposition)