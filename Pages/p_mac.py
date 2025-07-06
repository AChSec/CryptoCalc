import customtkinter as ctk
import hashlib
from texts import mac_info, hmac_info
import functions as f
from utils import insert_info


def mac(ctx):
    def run():
        try:
            ascii_code = f.text_to_ascii(str(entry_a.get()))
            key = entry_b.get()
            message = key + ascii_code
            h = hashlib.md5(message.encode()).hexdigest()
            ctx.output_label.configure(text=f"{entry_a.get()} in ASCII-Code: {ascii_code}\n\nSchlüssel {key} wird vorangestellt: {message}\n\nAus dem Ergebnis wird der MAC erstellt: {h}\n\nNur zur Veranschaulichung. Ein MAC auf Basis einer Block-Chiffre (DES, AES) entspricht der Block-Länge des verwendeten Verfahrens", font=("Roboto", 14))

        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
            return None
        
        
    def hmac():
        try:
            key = (entry_k.get())
            message = (entry_m.get())
            result = f.calc_hmac(key, message)
            ctx.output_label.configure(text=f"{result}", font=("Arial", 14), compound="top")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")        


    mac_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    mac_frame.pack(padx=5, pady=(0, 5), fill="both")
    mac_frame.columnconfigure((0, 4), weight=1)

    ctk.CTkLabel(mac_frame, text="MAC (demo)", 
                 font=("Roboto", 14, "bold"), anchor="center").grid(row=0, column=1, columnspan=3, pady=5)

    entry_a = ctk.CTkEntry(mac_frame, placeholder_text="Klartext", width=120)
    entry_b = ctk.CTkEntry(mac_frame, placeholder_text="Schlüssel", width=120)
    ctk.CTkButton(mac_frame, text="MAC", command=run, fg_color="#80350E", width=80).grid (row= 1, column = 3, padx=5, pady=5)

    entry_a.grid(row = 1, column = 1, padx =5,pady=5)
    entry_b.grid(row = 1, column = 2, padx=5, pady=5)
    
    hmac_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    hmac_frame.pack(fill="both", expand=True, padx=3, pady=2)
    hmac_frame.columnconfigure((0, 4), weight=1)

    ctk.CTkLabel(hmac_frame, text="HMAC-SHA256", 
                 font=("Roboto", 14, "bold"), anchor="center").grid(row=0, column=1, columnspan=3, pady=5)
    
    entry_k = ctk.CTkEntry(hmac_frame, placeholder_text="Schlüssel" , width=120)
    entry_m = ctk.CTkEntry(hmac_frame, placeholder_text="Klartext", width=120)
    ctk.CTkButton(hmac_frame, text="HMAC", command=hmac, fg_color="#80350E", width=80).grid (row= 1, column = 3, padx=5, pady=(5, 20))

    entry_k.grid(row = 1, column = 2, padx=5, pady=(5, 20))
    entry_m.grid(row = 1, column = 1, padx=5, pady=(5, 20))

    
    insert_info(ctx.info_box, "MAC", mac_info)
    insert_info(ctx.info_box, "HMAC", hmac_info)



