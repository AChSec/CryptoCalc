import customtkinter as ctk
from pages import pages, images
from utils import prepare_page, create_submenu_buttons, set_current_button, show_subframe, open_top_window, active_color, default_color
from context import PageContext


### System settings ###

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


### App design ###

app = ctk.CTk()
app.geometry("1000x550")
app.title("Kryptographie Rechner | Ch. Lönneker")

main_frame = ctk.CTkFrame(app, fg_color="#deebfc")  # Main frame with 2 rows and 3 columns
main_frame.pack(expand=True, fill="both")                                              
main_frame.grid_rowconfigure(0, weight=0)                                                
main_frame.grid_rowconfigure(1, weight=1)                                                   
main_frame.grid_columnconfigure(0, weight=0)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=0)

sidebar = ctk.CTkFrame(main_frame, width= 200, corner_radius=0, fg_color="#878f9a")   # 1st column: sidebar
sidebar.grid(row=0, column=0, rowspan=3, sticky="ns")

content = ctk.CTkFrame(main_frame, fg_color="#c9dcf5", border_color="#d4b05b", border_width=2)  # 2nd column upper part
content.grid(row=0, column=1, sticky="nsew", padx=10, pady=(10, 5))

output = ctk.CTkFrame(main_frame, width=350, fg_color="#deebfc")   # 3rd column: outputs
output.grid(row =0, column=2, rowspan=3, sticky="nsew", padx= 10, pady=10)
output.grid_rowconfigure(0, weight=0)
output.grid_rowconfigure(1, weight=1)


### General page design ###

# 3rd column: output header, scrollable frame & default text

ctk.CTkLabel(output, text="Ergebnis", font=("Roboto", 18)).grid(row=0, column=0, sticky ="new", pady=5)

output_frame = ctk.CTkScrollableFrame(output, fg_color="#deebfc", width=300)
output_frame.grid(row=1, column=0, rowspan=2, sticky="nsew", padx=10)

output_label = ctk.CTkLabel(output_frame, text="Bitte wähle eine Funktion aus\n", font=("Roboto", 14, "bold"), 
                            wraplength=230, width=260, height=120, anchor="n", justify="center")
output_label.pack(pady=10, padx=10, fill="both", expand=True)


# 2nd column: content header & empty infobox

header = ctk.CTkLabel(content, text="", font=("Roboto", 18))
header.pack(pady=5)

info_box = ctk.CTkTextbox(main_frame, wrap="word", font=("Roboto", 12), fg_color="#c9dcf5", border_color="#d4b05b", border_width=2, height=500)
info_box.grid(row=1, column=1, padx=10, pady=(5,10), sticky="nsew")

ctx = PageContext(header, content, info_box, output_label, images)


# 1st column: sidebar buttons (menu)


#------------ Main menus ------------#

names = ["rsa_subframe", "elgamal_subframe", "signature_subframe", "zkp_subframe", "hash_subframe"]
subframes = {}
for name in names:
    subframes[name] = ctk.CTkFrame(sidebar, fg_color="transparent")


small_buttons = [
#   Button                  Description (header)                    Page (pages)    Submenu             Row Column  Padx (left/right)
    ("Caesar", 	            "Caesar-Verschlüsselung",               "CAESAR",       None,               2,  0,      (10,5)),
    ("Spalten",             "Spaltentransposition",                 "COL_TRANS",    None,               2,  1,      (5,10)),
    ("a\u207B\u00B9 mod n", "Multiplikativ Inverses Element",       "M_INV",        None,               3,  0,      (10,5)),
    ("DH",       			"Diffie-Hellman Schlüsselaustausch",    "DH",           None,               3,  1,      (5,10)),
    ("RSA",                 "Rivest–Shamir–Adleman Verfahren (RSA)","RSA_INFO",     "rsa_subframe",     4,  0,      (10,5)),
    ("ElGamal",             "Das ElGamal Verfahren",                "ELGAMAL_INFO", "elgamal_subframe", 4, 1,       (5,10)),
    ("ECC", 				"Elliptische Kurven",                   "ECC",          None,               6,  0,      (10,5)),
    ("Signatur",            "Digitale Signaturen",                  "SIGNATURES",   "signature_subframe",6, 1,      (5,10)),
    ("Fermat", 				"Faktorisierungsmethode nach Fermat",   "FERMAT",       None,               8,  0,      (10,5)),
    ("BSGS", 				"Shanks' Baby-step Giant-step",         "BSGS",         None,               8,  1,      (5,10)),
    ("ZKP",                 "Zero-Knowledge Proof",                 "ZKP_INFO",     "zkp_subframe",     9,  0,      (10,5)),
    ("Hash/MAC",            "Kryptographische Hilfsfunktionen",     "AUXILIARIES",  "hash_subframe",    9,  1,      (5,10)),
]
for text, desc, page_key, subframe_key, row, col, padx in small_buttons:
    s = subframes.get(subframe_key) if subframe_key else None
    btn = ctk.CTkButton(sidebar, text=text, width=60, border_color="#003366", border_width=1)
    btn.configure(command= lambda d=desc, p=page_key, s=s, b=btn:
                  (prepare_page(d, ctx), pages[p](ctx), show_subframe(s, b) if s 
                   else (b.configure(fg_color=active_color), set_current_button(b))))
    btn.grid(row=row, column=col, pady=7, padx=padx, sticky="ew")


big_buttons = [
#   Button                  Description (header)                    Page (pages)                        Row         pady   Active color
    ("Home",                "Willkommen",                           "HOME",                             0,         (10,7), True),
    ("Sicherheitsdienste",  "Sicherheitsdienste",                   "SERVICES",                         12,             7, False),
    ("Sicherheitsmechanismen","Sicherheitsmechanismen",             "MECHANISMS",                       13,             7, False),
    ("Sicherheitsprotokolle","Sicherheitsprotokolle",               "PROTOCOLS",                        14,             7, False),
    ("About",               None,                                   None,                               16,             7, False)
]
for text, desc, page, row, pady, always_active in big_buttons:
    color = active_color if always_active else default_color
    btn = ctk.CTkButton(sidebar, text=text, width=180, fg_color=color, border_color="#003366", border_width=1)
    if page:
        btn.configure(command=lambda d=desc, p=page, b=btn, always=always_active: 
                      (prepare_page(d, ctx), pages[p](ctx), None if always
                       else (b.configure(fg_color=active_color), set_current_button(b))))
    else:
        btn.configure(command=lambda: open_top_window(app, ctx))
    btn.grid(row=row, columnspan=2, pady=pady, padx=10)


#------------ Submenus ------------#

submenus_data = {
    "rsa_subframe": [
        ("RSA Key", 			lambda: [prepare_page("RSA Schlüsselerzeugung", ctx, close=False),		pages["RSA_KEY"](ctx)], 		0),
        ("RSA Encrypt", 		lambda: [prepare_page("RSA Verschlüsselung", ctx, close=False),			pages["RSA_ENCRYPT"](ctx)], 	1),
        ("RSA Decrypt", 		lambda: [prepare_page("RSA Entschlüsselung", ctx, close=False),			pages["RSA_DECRYPT"](ctx)],		2)
    ],
    "elgamal_subframe": [
        ("Schlüsselerzeugung", 	lambda: [prepare_page("ElGamal Schlüsselgenerierung", ctx, close=False),pages["ELGAMAL_KEY"](ctx)], 	0),
        ("Verschlüsselung", 	lambda: [prepare_page("ElGamal Verschlüsselung", ctx, close=False),		pages["ELGAMAL_ENCRYPT"](ctx)], 1),
        ("Key Agreement", 		lambda: [prepare_page("ElGamal Schlüsselvereinbarung", ctx, close=False),pages["ELGAMAL_EXCHANGE"](ctx)],2)
    ],
    "signature_subframe": [
        ("Erzeugung", 			lambda: [prepare_page("Signatur-Erzeugung", ctx, close=False),			pages["SIGN"](ctx)], 			0),
        ("Verifikation",	 	lambda: [prepare_page("Signatur-Verifizierung", ctx, close=False),		pages["VERIFY"](ctx)], 			1),
    ],
    "zkp_subframe": [
        ("Fiat-Shamir",			lambda: [prepare_page("Fiat-Shamir Protokoll", ctx, close=False),		pages["FIAT-SHAMIR"](ctx)], 	0)		
    ],
    "hash_subframe": [
        ("Hash Func",			lambda: [prepare_page("Hash-Funktionen", ctx, close=False),		    	pages["HASH"](ctx)],		    0),
        ("PW Hash",				lambda: [prepare_page("Password Hashing", ctx, close=False),			pages["PW-HASHING"](ctx)],	    1),
        ("MAC/HMAC",			lambda: [prepare_page("Message Authentication Codes", ctx, close=False),pages["MAC"](ctx)],		        2)		
    ]
}
for subframe_name, buttons in submenus_data.items():
    for text, command, row in buttons:
        create_submenu_buttons(subframes[subframe_name], text, command, row)


#------------ Separator lines ------------#

separators = [{"row": 1, "color": "#d4b05b"}, {"row": 11, "color": "grey"}, {"row": 15, "color": "grey"}]

for sep in separators:
    ctk.CTkFrame(sidebar, height=3, width=200, fg_color=sep["color"]).grid(row=sep["row"], columnspan=2, pady=5)


### Start page ###

prepare_page("Willkommen", ctx)
pages["HOME"](ctx)


### Run app ###

app.mainloop()