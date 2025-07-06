import customtkinter as ctk
from texts import fermat_info
from functions import factorise
from utils import insert_info

def fermat(ctx):
    def run():
        try:
            n = int(entry_n.get())
            p, q = factorise(n)
            phi_n = (p-1) * (q-1)
            ctx.output_label.configure(text=f"p = {p}\nq = {q}\nphi_n = {phi_n}\n\n\nNächster Schritt: Multiplikativ Inverses Element von e im Modul phi_n", 
                                       font=("Roboto", 14), justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
    
    entry_n = ctk.CTkEntry(ctx.content, placeholder_text="Modul:")
    entry_n.pack(pady=5)
    
    ctk.CTkButton(ctx.content, text="Berechnen", command=run).pack(pady=10)

    image_frame = ctk.CTkFrame(ctx.content, fg_color="#d4b05b")
    image_frame.pack(fill="both", expand=True, pady=(20, 0))
    image = ctx.images.get("fermat")
    if image:
        ctk.CTkLabel(image_frame, image=image, text="", 
                     fg_color="#F5E5E5", corner_radius=5, width=200).pack(padx=2, pady=2, fill="both")
        
    insert_info(ctx.info_box, "Anwendung:", fermat_info)

