import customtkinter as ctk
from texts      import m_inverse_info
from functions  import m_inverse as m_inv
from utils      import insert_info


def m_inverse(ctx):
    def run():
        try:
            n, a, b = m_inv(int(entry_a.get()), int(entry_n.get()))
            if b:
                ctx.output_label.configure(text=f"a\u207B\u00B9 = {b}\n\n{a} * {b} modulo {n} ergibt {a * b % n}", font=("Roboto", 14))
            else:
                ctx.output_label.configure(text=f"Die Zahlen {a} und {n} sind nicht teilerfremd", font=("Roboto", 14), justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")

    entry_a = ctk.CTkEntry(ctx.content, placeholder_text="a:")
    entry_n = ctk.CTkEntry(ctx.content, placeholder_text="n:")
    entry_a.pack(pady=5)
    entry_n.pack(pady=5)
    
    ctk.CTkButton(ctx.content, text="Berechnen", command=run).pack(pady=10)

    image = ctx.images.get("gcd")
    if image:
        ctk.CTkLabel(ctx.content, image=image, text="", corner_radius=5).pack(expand=True, padx=3, pady=3, fill="both")

    insert_info(ctx.info_box, "Info", m_inverse_info)

