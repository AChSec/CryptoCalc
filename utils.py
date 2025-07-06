import customtkinter as ctk

current_subframe = None
current_button = None
default_color = "#3B8ED0" 	# default color for buttons
active_color = "#003366"	# active buttons (with submenu)


def open_top_window(app, ctx):							# opens another window with developer info (About)
    top = ctk.CTkToplevel(app)
    top.title("About")
    top.transient(app)
    top.geometry("300x400")
    ctk.CTkLabel(top, text="Christian Lönneker | Juni 2025").pack(pady=10)
    image = ctx.images.get("about")
    if image:
        ctk.CTkLabel(top, image=image, text="", 
                     fg_color="#f3f3f3", corner_radius=5, justify="center"
                     ).pack(expand=True, padx=2, pady=2, fill="both")


                    ### Sidebar behavior ###  

def create_submenu_buttons(subframe, text, command, row):
    b = ctk.CTkButton(master=subframe, text=text, command=command, 
                   width=120, fg_color="#5A5E61", border_color="#003366", border_width=1)
    b.grid(row=row, columnspan=2, pady=5, padx=10, sticky="ew")


def set_current_button(button):
    global current_button
    current_button = button


def close_subframes():								    # closes submenus, resets global variables and button default color. 
    global current_subframe, current_button				
    if current_subframe:								
        current_subframe.grid_forget()
        current_subframe = None
    if current_button:
        current_button.configure(fg_color=default_color)
        current_button = None


def show_subframe(subframe, button):				    # opens submenus (avalable for RSA, ElGamal, Signature, ZKP, and MAC/Hash)
    global current_subframe, current_button
    if current_subframe == subframe:					# closes submenu on second click 
        close_subframes()
    else:
        close_subframes()
        info = button.grid_info()
        button_row = int(info["row"])					# places submenu beneath main button
        subframe.grid(row=button_row + 1, column=0, columnspan=2, padx=10, sticky="")
        button.configure(fg_color=active_color)
        current_subframe = subframe
        current_button = button


                    ### Page design ###  

def clear_output(ctx):						            # clears content in the right-sided section (3rd column)
    ctx.output_label.configure(text="")						
    ctx.output_label.configure(text=f"Warte auf Berechnung\n", font=("Roboto", 14, "bold"), justify="center")


def clear_content(ctx):						            # clears content in the middle section (2nd column)
    for widget in ctx.content.winfo_children():				
        if widget != ctx.header:                        # header is changed by prepare_page function
            widget.destroy()
    ctx.info_box.configure(state="normal")
    ctx.info_box.delete("0.0", "end")


def prepare_page(new, ctx, close=True):					# used after click on any button
    clear_content(ctx)
    clear_output(ctx)
    ctx.header.configure(text=new)
    if close:											# close=True only for main buttons
        close_subframes()	


def create_image(frame, images, image_title):           # creates image with golden border frame
    image_frame = ctk.CTkFrame(frame, fg_color="#d4b05b")
    image_frame.pack(fill="both", expand=True, pady=(15, 0))
    image = images.get(image_title)
    if image:
        ctk.CTkLabel(image_frame, image=image, text="", fg_color="#f3f3f3", corner_radius=5).pack(expand=True, padx=2, pady=2, fill="both")


def create_input_grid(frame, placeholders: dict, positions: dict = None):
    entries = {}
    for k, label in placeholders.items():
        entry = ctk.CTkEntry(frame, placeholder_text=label, width=80)
        if positions:
            pos = positions.get(k)
            if isinstance(pos, tuple):
                row, col = pos
                entry.grid(row=row, column=col, padx=5, pady=5)
            elif isinstance(pos, dict):
                entry.grid(**pos)
            else:
                entry.pack(pady=5)
        else: entry.pack(pady=5)
        entries[k] = entry
    return entries


def insert_info(info_box, header, text):                # fills infobox with bold header and text from 'texts' file
    info_box.configure(state="normal")
    info_box._textbox.tag_configure("bold", font=("Roboto", 14, "bold"), justify = "left", spacing3=10)
    info_box._textbox.tag_configure("line", spacing2=5, spacing3=5)
    info_box._textbox.insert("end", f"{header}\n", "bold")
    info_box._textbox.insert("end", text, "line")
    info_box.configure(state="disabled")