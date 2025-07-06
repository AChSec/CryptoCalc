import customtkinter as ctk
import functions as f
from texts import elgamal_info, elgamal_application, elgamal_key_info, elgamal_encrypt_info, elgamal_exchange_info
from utils import insert_info, create_input_grid, create_image


def elgamal_main(ctx):
    ctk.CTkLabel(ctx.content, image=ctx.images["elgamal"], text="").pack(pady=10, anchor="center")
    
    create_image(ctx.content, ctx.images, "elgamal_sec")
    
    insert_info(ctx.info_box, "Info:", elgamal_info)
    insert_info(ctx.info_box, "Anwendung:", elgamal_application)
    


def elgamal_key(ctx):
    def run():
        try:
            p = int(entry_p.get())
            g = int(entry_g.get())
            d = int(entry_d.get())
            e = f.elgamal_key(p, g, d)
            ctx.output_label.configure(text=f"e = {e}\n\nVeröffentliche ({p}, {g}, {e})", font=("Roboto", 14), justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")

    entry_p = ctk.CTkEntry(ctx.content, placeholder_text="p:")
    entry_p.pack(pady=5)
    entry_g = ctk.CTkEntry(ctx.content, placeholder_text="g:")
    entry_g.pack(pady=5)
    entry_d = ctk.CTkEntry(ctx.content, placeholder_text="d vorgeben:")
    entry_d.pack(pady=5)

    ctk.CTkButton(ctx.content, text="Berechnen", command=run).pack(pady=10)

    image = ctx.images.get("key")
    if image:
        ctk.CTkLabel(ctx.content, image=image, text="").pack(pady=10, anchor="n")

    insert_info(ctx.info_box, "Schritte:", elgamal_key_info)



def elgamal_encrypt(ctx):
    def run():
        try:
            x = int(entry_x.get())
            p = int(entries["p"].get())
            g = int(entries["g"].get())
            e = int(entries["e"].get())
            k = int(entries["k"].get())
            a, b = f.elgamal_encrypt(x, p, g, e, k)
            ctx.output_label.configure(text=f"a = {a}\nb = {b}", font=("Roboto", 14), justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")

    insert_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    insert_frame.pack()

    entry_x = ctk.CTkEntry(insert_frame, placeholder_text="x:", width=170)
    entry_x.grid(row = 0, column = 0, columnspan=2, padx=5, pady=5)
    
    placeholders = {"p": "p", "g": "g", "e": "e", "k": "k"}
    grid_positions = {"p": (1,0), "g": (1,1), "e": (2,0), "k": (2,1)}
    entries = create_input_grid(insert_frame, placeholders, grid_positions)

    ctk.CTkButton(ctx.content, text="Berechnen", command=run).pack(pady=10)

    create_image(ctx.content, ctx.images, "elgamal_encr")

    insert_info(ctx.info_box, "Info:", elgamal_encrypt_info)


def elgamal_exchange(ctx):
    def run_alice():
        try:
            p = int(entries["p"].get())
            g = int(entries["g"].get())
            e = int(entries["e"].get())
            k = int(entries["k"].get())
            a, key = f.elgamal_exchange_A(p, g, e, k)
            ctx.output_label.configure(text=f"a = {a}\nAlice Key = {key}", font=("Roboto", 14), justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
    
    def run_bob():
        try:
            a = int(entries["a"].get())
            d = int(entries["d"].get())
            p = int(entries["p"].get())
            key = f.elgamal_exchange_B(a, d, p)
            ctx.output_label.configure(text=f"Bob Key = {key}", font=("Roboto", 14), justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")

    
    insert_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    insert_frame.pack()

    ctk.CTkLabel(insert_frame, text="Alice").grid(row = 0, column = 0, columnspan=2, padx=5, pady=5)
    ctk.CTkLabel(insert_frame, text="Bob").grid(row = 0, column = 2, columnspan=2, padx=5, pady=5)

    placeholders = {"p": "p", "g": "g", "e": "e", "k": "k", "a": "a", "d": "d"}
    grid_positions = {"p": (1,0), "g": (1,1), "e": (2,0), "k": (2,1), "a": (1,2), "d":(1,3)}
    entries = create_input_grid(insert_frame, placeholders, grid_positions)

    ctk.CTkButton(insert_frame, text="Berechnen", command=run_alice, width=120).grid(row= 3, column=0, columnspan=2, pady=10)
    ctk.CTkButton(insert_frame, text="Berechnen", command=run_bob, width=120).grid(row= 3, column=2, columnspan=2, pady=10)

    create_image(ctx.content, ctx.images, "elgamal_exch")

    insert_info(ctx.info_box, "Info:", elgamal_exchange_info)
