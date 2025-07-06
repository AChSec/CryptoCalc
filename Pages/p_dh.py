import customtkinter as ctk
from texts      import diffie_hellman_info
from functions  import dh_exchange
from utils      import insert_info, create_input_grid

def diffie_hellman(ctx):
    def run():
        try:
            p = int(entries["p"].get())
            g = int(entries["g"].get())
            a = int(entries["a"].get())
            b = int(entries["b"].get())
            alpha, beta, key = dh_exchange(p, g, a, b)
            ctx.output_label.configure(text=f"Alice sendet α = {alpha}\n\nBob rechnet α ** b mod p = {key} = K\n\nBob sendet β = {beta}\n\nAlice rechnet β ** a mod p = {key} = K", 
                          font=("Roboto", 14), 
                          justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
    
    
    input_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    input_frame.pack()
    
    placeholders = {"p": "Modul p", "g": "Basis g", "a": "a", "b": "b"}
    grid_positions = {  "p": (0,0), "g": (0,1), "a": (1,0), "b": (1,1)}
    entries = create_input_grid(input_frame, placeholders, grid_positions)
    
    ctk.CTkButton(input_frame, text="Berechnen", command=run, width=120).grid(row= 2, column=0, columnspan=2, pady=10)
    
    image_frame = ctk.CTkFrame(ctx.content, fg_color="#d4b05b")
    image_frame.pack(fill="both", expand=True, pady=(10, 0))

    image = ctx.images.get("dh_exchange")
    if image:
        ctk.CTkLabel(image_frame, image=image, text="", fg_color="#f3f3f3").pack(padx=2, pady=2, expand=True, fill="both")

    insert_info(ctx.info_box, "Info", diffie_hellman_info)
