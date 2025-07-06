import customtkinter as ctk
import functions as f
from texts import zkp_info, fiat_shamir_info
from utils import insert_info, create_input_grid, create_image


def zero_knowledge_info(ctx):

    border_frame = ctk.CTkFrame(ctx.content, fg_color="#d4b05b")
    border_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))
    image = ctx.images.get("zkp_info")
    if image:
        ctk.CTkLabel(border_frame, image=image, text="", 
               width=200, fg_color="#f3f3f3").pack(padx=2, pady=2, fill="both")
        
    insert_info(ctx.info_box, "Zero-Knowledge Proof in der Kryptographie", zkp_info)

def fiat_shamir(ctx):
    def commitment():
        try:
            k = int(entries["k"].get())
            n = int(entries["n"].get())
            x = (k **2 % n)
            ctx.output_label.configure(text=f"{k}² mod {n} = {x}", 
                                       font=("Roboto", 14), justify="left")
            ctx.info_box.configure(state="normal")
            ctx.info_box.insert("end", f"\n\n*** Commitment ist erfolgt: {x} ***")
            ctx.info_box.configure(state="disabled")
            entries["x"].delete(0, "end")
            entries["x"].insert(0, int(x))
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")

    def run():
        try:
            n = int(entries["n"].get())
            s = int(entries["s"].get())
            k = int(entries["k"].get())
            r_bit = bit.get()
            v, x, y = f.fiat_shamir(n, s, k, r_bit)
            ctx.output_label.configure(text=f"Öffentlicher Schlüssel: {n}, {v}\nCommitment: {x}\nResponse: {y}", 
                                       font=("Roboto", 14), justify="left")
            entries["v"].delete(0, "end")
            entries["v"].insert(0, int(v))
            entries["y"].delete(0, "end")
            entries["y"].insert(0, int(y))

        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
    
    def verification():
        try:
            n = int(entries["n"].get())
            v = int(entries["v"].get())
            x = int(entries["x"].get())
            y = int(entries["y"].get())
            r_bit = bit.get()
            check = f.fiat_shamir_verification(n, v, x, y, r_bit)
            ctx.output_label.configure(text=f"{check}", font=("Roboto", 14), justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")


    ### Build page with entry fields, buttons, and image

    insert_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    insert_frame.pack()

    labels = [("Bob", 0, 0), ("Alice", 0, 1), ("Bob", 0, 2), ("Alice", 0, 3)]
    for text, row, col in labels:
        ctk.CTkLabel(insert_frame, text=text).grid(row=row, column=col, padx=5, pady=5)
    
    placeholders = {"n": "n", "k": "k", "s": "s", "v": "v", "x": "x", "y": "y"}
    grid_positions = {  "n": (1,0), "v": (1,2), "x": (1,3),
                        "k": (2,0), "s": (2,2), "y": (2,3)}
    entries = create_input_grid(insert_frame, placeholders, grid_positions)

    bit = ctk.IntVar(value=0)

    frame_radio = ctk.CTkFrame(insert_frame, fg_color="#c9dcf5")
    frame_radio.grid(row = 1, column=1, rowspan=4, pady=5)

    ctk.CTkRadioButton(frame_radio, text="0", variable=bit, value=0, width=80).grid(row=0, column=0, padx=5, pady=5)
    ctk.CTkRadioButton(frame_radio, text="1", variable=bit, value=1, width=80).grid(row=1, column=0, padx=5, pady=5)

    ctk.CTkLabel(frame_radio, text="Challenge", 
                 text_color="#003366", font=("Roboto", 14, "bold"), anchor="s"
                 ).grid(row = 4, column = 0, padx=5, pady=7)


    ctk.CTkButton(insert_frame, text="Commit", command=commitment, width=80).grid(row= 4, column=0, pady=10)
    ctk.CTkButton(insert_frame, text="Berechnen", command=run, width=80).grid(row= 4, column=2, pady=10)
    ctk.CTkButton(insert_frame, text="Check", command=verification, width=80).grid(row= 4, column=3, pady=10)

    create_image(ctx.content, ctx.images, "zkp")

    insert_info(ctx.info_box, "Info", fiat_shamir_info)

