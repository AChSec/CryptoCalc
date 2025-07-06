import customtkinter as ctk
from texts      import bsgs_info
from functions  import babystep_giantstep
from utils      import insert_info, create_input_grid

def bsgs(ctx):
    def run():
        try:
            p = int(entries["p"].get())
            g = int(entries["g"].get())
            e = int(entries["e"].get())
            result = babystep_giantstep(p, g, e)
            ctx.output_label.configure(text=f"Ergebnis: {result}")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
            
    input_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    input_frame.pack(fill="both", expand=True, padx=3, pady=2, anchor="center")
    input_frame.columnconfigure((0, 4), weight=1)
    
    placeholders = {"p": "p", "g": "g", "e": "e"}
    grid_positions = {  "p": (0,1), "g": (0,2), "e": (0,3)}
    entries = create_input_grid(input_frame, placeholders, grid_positions)

    ctk.CTkButton(ctx.content, text="Berechnen", command=run).pack(pady=10)

    image_frame = ctk.CTkFrame(ctx.content, fg_color="#d4b05b")
    image_frame.pack(fill="both", expand=True, pady=(20, 0))
    image = ctx.images.get("bsgs")
    if image:
        ctk.CTkLabel(image_frame, image=image, text="", 
               fg_color="#F5E5E5", corner_radius=5, width=200).pack(padx=2, pady=2, fill="both")
        
    insert_info(ctx.info_box, "Anwendung:", bsgs_info)
