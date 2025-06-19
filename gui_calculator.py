import math

from calc import tokenize, is_number, precedence

import tkinter as tk

import customtkinter as ctk

themes = {
    "dark": {
        "bg": "#2B2B2B",
        "fg": "#3C3C3C",
        "text": "#FFFFFF",
        "hover": "#565956",
        "entry_bg": "#333333",
    },
    "light": {
        "bg": "#F5F5F5",
        "fg": "#E0E0E0",
        "text": "#000000",
        "hover": "#686C70",
        "entry_bg": "#FFFFFF",
    },
    "Joy pastel": {
        "bg": "#FFF3E0",
        "fg": "#FFE0B2",
        "text": "#4A2C00",
        "hover": "#FF9800",
        "entry_bg": "#FFF8E7",
    }
}



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Calculator")
window.geometry("417x550")
window.resizable(False, False)

main_frame = ctk.CTkFrame(window, corner_radius=10)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

display_text = tk.StringVar()
display = ctk.CTkEntry(
    main_frame,
    textvariable=display_text,
    font=("Helvetica", 26), 
    justify="right",
    height=60,
    corner_radius=10,
    state="normal" 
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 20), sticky="ew")


def on_click(value):
    expression = display_text.get()
    if value in ["/","*","+","-"]:
       expression = expression + " " + value + " "    
    else:
       expression = expression + value
    display_text.set(expression)
       

def on_clear():
  display_text.set("")

def on_equal():
  try:
    expr = display_text.get()
    exprresult = " ".join(expr.split())
    print(exprresult)
    ans = str(tokenize(exprresult))
    print(ans)
    display_text.set(ans)
    

  except Exception as e:
    display_text.set("Error: Invalid Expression")
    window.after(2000, lambda: display_text.set(""))


buttons = [
    ("C", on_clear, 1, 0, 2),
    ("/", lambda: on_click("/"), 1, 2, 1),
    ("*", lambda: on_click("*"), 1, 3, 1),
    ("7", lambda: on_click("7"), 2, 0, 1),
    ("8", lambda: on_click("8"), 2, 1, 1),
    ("9", lambda: on_click("9"), 2, 2, 1),
    ("-", lambda: on_click("-"), 2, 3, 1),
    ("4", lambda: on_click("4"), 3, 0, 1),
    ("5", lambda: on_click("5"), 3, 1, 1),
    ("6", lambda: on_click("6"), 3, 2, 1),
    ("+", lambda: on_click("+"), 3, 3, 1),
    ("1", lambda: on_click("1"), 4, 0, 1),
    ("2", lambda: on_click("2"), 4, 1, 1),
    ("3", lambda: on_click("3"), 4, 2, 1),
    ("=", on_equal, 4, 3, 1),
    ("0", lambda: on_click("0"), 5, 0, 2), 
    (".", lambda: on_click("."), 5, 2, 1),
]


def apply_theme(theme_name):
    theme = themes[theme_name]
    ctk.set_appearance_mode("light" if theme_name == "light" else "dark") 
    main_frame.configure(fg_color=theme["bg"])
    display.configure(
        fg_color=theme["entry_bg"],
        text_color=theme["text"],
    )
    for widget in main_frame.winfo_children():
        if isinstance(widget, ctk.CTkButton):
            widget.configure(
                fg_color=theme["fg"],
                text_color=theme["text"],
                hover_color=theme["hover"]
            )
    window.configure(bg=theme["bg"])  

theme_var = tk.StringVar(value="dark")
theme_menu = ctk.CTkOptionMenu(
    main_frame,
    values=list(themes.keys()),
    variable=theme_var,
    command=apply_theme,
    font=("Helvetica", 14),
    width=120,
    corner_radius=10
)
theme_menu.grid(row=6, column=0, columnspan=4, pady=10, sticky="ew")

for text, command, row, col, colspan in buttons:
    button = ctk.CTkButton(
        main_frame,
        text=text,
        command=command,
        font=("Helvetica", 18),
        width=80 if colspan == 1 else 170, 
        height=60, 
        corner_radius=15, 
        hover_color=themes[theme_var.get()]["hover"],
        fg_color=themes[theme_var.get()]["fg"],
        text_color=themes[theme_var.get()]["text"],
        border_width=0
    )
    button.grid(row=row, column=col, columnspan=colspan, padx=7, pady=7, sticky="ew")



apply_theme("dark")

window.mainloop()




























