import customtkinter as ctk
from texts import ecc_info
import functions as f
from utils import insert_info, create_input_grid, create_image

def point_addition(ctx):
    def run():
        try:
            xp = int(entries["xp"].get())
            xq = int(entries["xq"].get())
            yp = int(entries["yp"].get())
            yq = int(entries["yq"].get())
            n =  int(entries["n"].get())
            if xp == xq and yp == yp: 
                ctx.output_label.configure(text=f"Berechnung mit dieser Funktion nicht möglich (Xp und Xq dürfen nicht identisch sein)", anchor="nw", justify="left")
            else: 
                xr, yr = f.point_addition(xp, yp, xq, yq, n)
                ctx.output_label.configure(text=f"Ergebnis: Der Punkt R hat die Koordinaten R({xr}|{yr})", font=("Roboto", 14), anchor="nw", justify="left")
        except Exception as e:
            ctx.output_label.configure(text=f"Fehler: {e}")
            

    insert_frame = ctk.CTkFrame(ctx.content, fg_color="#c9dcf5")
    insert_frame.pack()

    placeholders = {"xp": "xp", "yp": "yp", "xq": "xq", "yq": "yq", "n": "n"}
    grid_positions = { "xp": (0,1), "yp": (0,3),
                       "xq": (1,1), "yq": (1,3),
                       "n":  (4,1)}
    entries = create_input_grid(insert_frame, placeholders, grid_positions)

    ctk.CTkLabel(insert_frame, text="P").grid(row=0, column=0, sticky="w", padx=5)
    ctk.CTkLabel(insert_frame, text="|").grid(row=0, column=2, sticky="w", padx=5)
    ctk.CTkLabel(insert_frame, text="Q").grid(row=1, column=0, sticky="w", padx=5)
    ctk.CTkLabel(insert_frame, text="|").grid(row=1, column=2, sticky="w", padx=5)
    ctk.CTkLabel(insert_frame, text="Modul").grid(row=4, column=0, sticky="w", padx=5)

    ctk.CTkButton(ctx.content, text="Punktaddition", command=run).pack(pady=10)

    create_image(ctx.content, ctx.images, "ecc")

    
    ### Infobox ###
    
    insert_info(ctx.info_box, "Anwendung:", ecc_info)

