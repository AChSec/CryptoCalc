import customtkinter as ctk
from functions import create_hash, pw_hash
from texts import hash_functions_info, pw_hash_info
from utils import insert_info


def auxiliaries_main(ctx):
    image_frame = ctk.CTkFrame(ctx.content, fg_color="#d4b05b")
    image_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))
    image = ctx.images.get("auxiliaries")
    if image:
        ctk.CTkLabel(image_frame, image=image, text="", 
               width=200, fg_color="#f3f3f3").pack(padx=2, pady=2, fill="both")
        
    insert_info(ctx.info_box, "Hash-Funktionen", hash_functions_info)
    insert_info(ctx.info_box, "MAC/HMAC", "Gewährleisten zusätzlich Authentizität. Weitere Infos im Menüpunkt MAC/HMAC")


def hash_function(ctx):
    def run():
        try:
            text = entry_m.get()
            algo = hash_algo_var.get()
            result, length = create_hash(text, algo)
            ctx.output_label.configure(text=f"{result}{length}", font=("Arial", 14))
            
            ctx.info_box.configure(state="normal")
            ctx.info_box.insert("end", f"Ergebnis: {result}")
            ctx.info_box.configure(state="disabled")

            if algo == "md5":
                        ctx.output_label.configure(text=f"{result}{length}\n\nAchtung, Verfahren ist nicht mehr sicher!")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
            
    entry_m = ctk.CTkEntry(ctx.content, placeholder_text="Message:", width=200)
    entry_m.pack(pady=5)
    hash_algo_var = ctk.StringVar(value="md5") 
    
    frame_radio = ctk.CTkFrame(ctx.content, fg_color="#deebfc", border_color="#d4b05b", border_width=1)
    frame_radio.pack(pady=5)
    
    hash_functions = [
        ("MD5",     "md5",    0, 0),
        ("SHA1",    "sha1",   0, 1),
        ("SHA256",  "sha256", 0, 2),
        ("SHA384",  "sha384", 1, 0),
        ("SHA512",  "sha512", 1, 1)
    ]

    for text, value, row, col in hash_functions:
          ctk.CTkRadioButton(frame_radio, text=text, 
                             variable=hash_algo_var, 
                             value=value
                             ).grid(row=row, column=col, padx=10, pady=5)

    ctk.CTkButton(ctx.content, text="Berechnen", command=run).pack(pady=10)
        
    insert_info(ctx.info_box, "Kopierfreundliche Ausgabe:", "")


def pw_hashing(ctx):
    def run():
        try:
            username = entry_id.get()
            password = entry_pw.get()
            if pw_hash(username, password):
                ctx.output_label.configure(text=f"Passwort korrekt", font=("Roboto", 14))
            else:
                ctx.output_label.configure(text=f"Fehler: Überprüfe Eingaben", font=("Roboto", 14))

        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}") 

    entry_id = ctk.CTkEntry(ctx.content, placeholder_text="Username:", width=200)
    entry_id.pack(pady=5)
    entry_pw = ctk.CTkEntry(ctx.content, placeholder_text="Password:", width=200)
    entry_pw.pack(pady=5)

    ctk.CTkButton(ctx.content, text="Login", command=run, width=120).pack(pady=10)

    image_frame = ctk.CTkFrame(ctx.content, fg_color="#d4b05b")
    image_frame.pack(fill="both", expand=True, padx=0, pady=(5, 0))
    image = ctx.images.get("user_database")
    if image:
        ctk.CTkLabel(image_frame, image=image, text="", 
               width=200, fg_color="#f3f3f3").pack(padx=2, pady=2, fill="both")
        
    insert_info(ctx.info_box, "Passwort-Datenbanken", pw_hash_info)

