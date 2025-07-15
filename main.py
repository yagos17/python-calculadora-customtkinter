import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Calculadora")
app.geometry("300x370")

current_expression = ""

def button_click(value):
    global current_expression

    display.configure(state="normal")

    if value == "C":
        current_expression = ""
    elif value == "=":
        try:
            result = str(eval(current_expression))
            current_expression = result
        except (SyntaxError, ZeroDivisionError, TypeError):
            current_expression = "Erro"
    elif value == "⌫":
        current_expression = current_expression[:-1]
    else:
        current_expression += value

    display.delete(0, ctk.END)
    display.insert(0, current_expression)
    display.configure(state="readonly")

display_font = ctk.CTkFont(family="Arial", size=25, weight="bold")

display = ctk.CTkEntry(master=app, font=display_font, state="readonly")
display.pack(pady=10, fill="x", padx=10)

button_frame = ctk.CTkFrame(master=app)
button_frame.pack(pady=20, padx=10)

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
    ("C", 4, 0), ("⌫", 4, 1)
]

for (text, row, col) in buttons:
    btn = ctk.CTkButton(master=button_frame, text=text, width=60, height=40, corner_radius=12, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

app.mainloop()