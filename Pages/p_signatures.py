import customtkinter as ctk
from functions import rsa_sign, elgamal_sign,  rsa_check, elgamal_check
from texts import digital_signature1, digital_signature2
from utils import insert_info, create_input_grid


def signature_main(ctx): 						

    image_frame = ctk.CTkFrame(ctx.content, fg_color="#d4b05b")
    image_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))
    image = ctx.images.get("signature")
    if image:
        ctk.CTkLabel(image_frame, image=image, text="", 
               width=200, fg_color="#f3f3f3").pack(padx=2, pady=2, fill="both")
        
    insert_info(ctx.info_box, "Digitale Signatur mit Nachrichten-Rückgewinnung", digital_signature1)
    insert_info(ctx.info_box, "Digitale Signatur mit Hashwert-Anhang", digital_signature2)


def create_signature(ctx):
    def run_rsa():
        try:
            x = int(entries_rsa["x"].get())
            d = int(entries_rsa["d"].get())
            n = int(entries_rsa["n"].get())
            s = rsa_sign(x, d, n)
            ctx.output_label.configure(text=f"s = {s}")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")

    def run_elgamal():
        try:
            p = int(entries["p"].get())
            g = int(entries["g"].get())
            e = int(entries["e"].get())
            d = int(entries["d"].get())
            r = int(entries["r"].get())
            m = int(entries["m"].get())
            h, m, s, rho = elgamal_sign(p, g, d, r, m)
            ctx.output_label.configure(text=f"Gesendet werden:\n\nMessage m: {m}\n\nSignaturelement s: {s}\n\nNachrichtenbezeichner rho: {rho}\n\nHashwert-Anhang: \n{h}\n\n(Kopierfreundlich in Infobox)", font=("Arial", 14), justify="left")
            ctx.info_box.configure(state="normal")
            ctx.info_box.delete("2.0", "end")
            ctx.info_box.insert("2.0", f"\n{h}")
            ctx.info_box.configure(state="disabled")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
            
    inserts_rsa = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    inserts_rsa.pack(padx=5, pady=5, fill="both")
    inserts_rsa.columnconfigure((0, 4), weight=1)

    ctk.CTkLabel(inserts_rsa, text="RSA mit Nachrichten-Rückgewinnung", font=("Roboto", 14), anchor="center").grid(row = 0, column = 1, columnspan=3, pady=5)
    
    placeholders = {"x": "x", "d": "d", "n": "n"}
    grid_positions = {"x": (1,1), "d": (1,2), "n": (1,3)}
    entries_rsa = create_input_grid(inserts_rsa, placeholders, grid_positions) 

    ctk.CTkButton(inserts_rsa, text="Berechnen", command=run_rsa, anchor="center").grid (row= 3, column = 1, columnspan=3, padx=5, pady=5)

    ctk.CTkLabel(inserts_rsa, image=ctx.images["rsa_sign"], text="").grid(row = 2, column=1, columnspan=3,padx=2, pady=2)


    insert_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5", border_color="#deebfc", border_width=2)
    insert_frame.pack(padx=5, pady=(0, 5), fill="both")
    insert_frame.columnconfigure((0, 4), weight=1)

    ctk.CTkLabel(insert_frame, text="ElGamal mit Hashwert-Anhang", font=("Roboto", 14), anchor="center").grid(row = 0, column = 1, columnspan=3, pady=5)

    placeholders = {"p": "p", "g": "g", "e": "e", "d": "d", "r": "r", "m": "m"}
    grid_positions = {"p": (2,1), "g": (2,2), "e": (2,3), "d": (4,1), "r": (4,2), "m": (4,3)}
    entries = create_input_grid(insert_frame, placeholders, grid_positions)

    ctk.CTkButton(insert_frame, text="Berechnen", command=run_elgamal, anchor="center").grid (row= 6, column = 1, columnspan=3, padx=5, pady=5)

    ctk.CTkLabel(insert_frame, image=ctx.images["elgamal_sign"], text="").grid(row = 5, column=1, columnspan=3,padx=2, pady=2)

    insert_info(ctx.info_box, "ElGamal Hashwert-Anhang:", "Warte auf Berechnung")



def verification(ctx):                  # page with verification options for both RSA and ElGamal
    
    def verify_rsa():
        try:
            e = int(entries["e"].get())
            n = int(entries["n"].get())
            s = int(entries["s"].get())
            x = int(entries["s"].get())
            result = rsa_check(e, n, s, x)              # returns 'valid' or 'invalid' as string
            ctx.output_label.configure(text=f"{result}", font=("Roboto", 14), compound="top")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")

    def verify_elgamal():
        try:
            p =     int(entries2["p"].get())
            g =     int(entries2["g"].get())
            e =     int(entries2["e"].get())
            rho =   int(entries2["rho"].get())
            s =     int(entries2["s"].get())
            m =     int(entries2["m"].get())
            result = elgamal_check(p, g, e, rho, s, m)  # returns 'valid' or 'invalid' as string
            ctx.output_label.configure(text=f"{result}", font=("Roboto", 14), compound="top")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")


    ### RSA entry fields and button, formulas are provided as images ###

    input_frame_rsa = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    input_frame_rsa.pack(fill="both", expand=True, padx=3, pady=2, anchor="center")
    input_frame_rsa.columnconfigure((0, 4), weight=1)
    
    ctk.CTkLabel(input_frame_rsa, text="RSA mit Nachrichten-Rückgewinnung", 
                 font=("Roboto", 14), anchor="center").grid(row=0, column=1, columnspan=3, pady=(2,5))	

    placeholders = {"e": "e", "n": "n", "s": "s", "x": "x"}
    grid_positions = {  "e": (1,1), "n": (1,2), "s": (1,3),
                        "x": (2,1)}
    entries = create_input_grid(input_frame_rsa, placeholders, grid_positions)
    
    image = ctx.images.get("rsa_verify")
    if image:
            ctk.CTkLabel(input_frame_rsa, image=image, text="").grid(row = 3, column=1, columnspan=3, padx=2, pady=2)
 
    ctk.CTkButton(input_frame_rsa, text="Verifiziere", command=verify_rsa, 
                  width=80).grid (row= 4, column = 2, padx=5, pady=5)


    ### ElGamal entry fields and button, formulas are provided as images###

    input_frame_elgamal = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5", border_color="#deebfc", border_width=2)
    input_frame_elgamal.pack(fill="both", expand=True, padx=5, pady=(0, 5), anchor="center")
    input_frame_elgamal.columnconfigure((0, 4), weight=1)
    
    ctk.CTkLabel(input_frame_elgamal, text="ElGamal mit Hashwert-Anhang", 
                 font=("Roboto", 14), anchor="center").grid(row=0, column=1, columnspan=3, pady=5)	

    placeholders2 = {"p": "p", "g": "g", "e": "e", "rho": "rho", "s": "s", "m": "H(m)"}
    grid_positions2 = {  "p": (1,1), "g": (1,2), "e": (1,3),
                       "rho": (2,1), "s": (2,2), "m": (2,3)}
    entries2 = create_input_grid(input_frame_elgamal, placeholders2, grid_positions2)
    
    image = ctx.images.get("elgamal_verify")
    if image:
            ctk.CTkLabel(input_frame_elgamal, image=image, text="").grid(row = 3, column=1, columnspan=3, padx=2, pady=2)
 
    ctk.CTkButton(input_frame_elgamal, text="Verifiziere", command=verify_elgamal, 
                  width=80).grid (row= 4, column = 2, padx=5, pady=5)


    insert_info(ctx.info_box, "Anwendung:", "Digital Signature Algorithm (DSA)")

    
