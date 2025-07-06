import customtkinter as ctk
import functions as f
from texts import rsa_info, rsa_application, rsa_key_info, rsa_encrypt_info, rsa_decrypt_info
from utils import insert_info, create_input_grid, create_image


### Main page with image and info ###

def rsa_main(ctx):
    ctk.CTkLabel(ctx.content, image=ctx.images["rsa"], text="").pack(pady=10, anchor="center")

    create_image(ctx.content, ctx.images, "rsa_sec")

    insert_info(ctx.info_box, "Info:", rsa_info)
    insert_info(ctx.info_box, "Anwendung:", rsa_application)


### Generating RSA key ###

def rsa_key(ctx):
    def run():
        try:
            p = int(entry_p.get())
            q = int(entry_q.get())
            e = int(entry_e.get())
            n, e, d, phi_n = f.rsa_key(p, q, e)
            ctx.output_label.configure(text=f"n = {n}\ne = {e}\nd = {d}\nphi_n = {phi_n}", font=("Roboto", 14), justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
    
    ctk.CTkLabel(ctx.content, image=ctx.images["key"], text="").pack(pady=10, anchor="n")
    
    entry_p = ctk.CTkEntry(ctx.content, placeholder_text="p:")
    entry_p.pack(pady=5)
    entry_q = ctk.CTkEntry(ctx.content, placeholder_text="q:")
    entry_q.pack(pady=5)
    entry_e = ctk.CTkEntry(ctx.content, placeholder_text="e vorgeben:")
    entry_e.pack(pady=5)

    ctk.CTkButton(ctx.content, text="Berechnen", command=run).pack(pady=10)

    insert_info(ctx.info_box, "Schritte:", rsa_key_info)


### Text to ASCII and Encryption ###

def rsa_encrypt(ctx):

    def convert():
        zahl = f.text_to_ascii(entry_text.get())
        ctx.output_label.configure(text=f"ASCII Code = {zahl}", font=("Roboto", 14), justify="left")

    def run():
        try:
            n = int(entries["n"].get())
            e = int(entries["e"].get())
            x = int(entries["x"].get())
            result = f.rsa_encrypt(n, e, x)
            ctx.output_label.configure(text=f"y = {result}", font=("Roboto", 14), justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")

    input_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    input_frame.pack(fill="both", expand=True, padx=3, pady=2, anchor="center")
    input_frame.columnconfigure((0, 5), weight=1)

    placeholders = {"x": "x", "n": "n", "e": "e"}
    grid_positions = {"x": (1,1), "n": (1,2), "e": (1,3)}
    entries = create_input_grid(input_frame, placeholders, grid_positions)

    entry_text = ctk.CTkEntry(input_frame, placeholder_text="Klartext", width=170)
    entry_text.grid(row=0, column=1, columnspan=2, padx=5, pady=(10, 5))

    ctk.CTkButton(input_frame, text="Convert", command=convert, width=80).grid(row=0, column=3, padx=5, pady=(10,5))
    ctk.CTkButton(input_frame, text="Berechnen", command=run, width=110).grid(row=1, column=4, padx=5, pady=5)

    create_image(ctx.content, ctx.images, "rsa_encr")

    insert_info(ctx.info_box, "Info:", rsa_encrypt_info)


### Decryption and ASCII to text ###

def rsa_decrypt(ctx):
    
    def convert():
        text = f.ascii_to_text(entry_text.get())
        ctx.output_label.configure(text=f"Klartext = {text}", font=("Roboto", 14), justify="left")
    
    def run():
        try:
            n = int(entries["n"].get())
            d = int(entries["d"].get())
            y = int(entries["y"].get())
            result = f.rsa_encrypt(n, d, y)
            ctx.output_label.configure(text=f"x = {result}", font=("Roboto", 14))
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")

    input_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    input_frame.pack(fill="both", expand=True, padx=3, pady=2, anchor="center")
    input_frame.columnconfigure((0, 5), weight=1)

    placeholders = {"y": "y", "n": "n", "d": "d"}
    grid_positions = {"y": (0,1), "n": (0,2), "d": (0,3)}
    entries = create_input_grid(input_frame, placeholders, grid_positions)

    entry_text = ctk.CTkEntry(input_frame, placeholder_text="ASCII Code", width=175)
    entry_text.grid(row=1, column=1, columnspan=2, padx=5)

    ctk.CTkButton(input_frame, text="Convert", command=convert, width=80).grid(row=1, column=3, padx=5, pady=5)
    ctk.CTkButton(input_frame, text="Berechnen", command=run, width=110).grid(row=0, column=4, padx=5, pady=(5, 10))

    create_image(ctx.content, ctx.images, "rsa_decr")


    insert_info(ctx.info_box, "Info:", rsa_decrypt_info)
