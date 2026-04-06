import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x550")
window.resizable(False, False)  # Prevent resizing

# Functions
def click(item):
    display.insert(tk.END, item)

def clear():
    display.delete(0, tk.END)

def equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Display
display = tk.Entry(window, width=16, font=("Arial", 30), borderwidth=5, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Button style
btn_params = {"width":4, "height":2, "font":("Arial", 20), "bd":3, "relief":"raised"}

# Number buttons layout
button_texts = [
    ('7','8','9'),
    ('4','5','6'),
    ('1','2','3'),
    ('.','0','=')
]

# Create number and equal/decimal buttons
for r, row in enumerate(button_texts, start=1):
    for c, text in enumerate(row):
        if text == '=':
            btn = tk.Button(window, text=text, **btn_params, bg="#4CAF50", fg="white", command=equal)
        elif text == '.':
            btn = tk.Button(window, text=text, **btn_params, bg="#FFC107", command=lambda t=text: click(t))
        else:
            btn = tk.Button(window, text=text, **btn_params, command=lambda t=text: click(t))
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Operator buttons
operators = [
    ('+',1), ('-',2), ('*',3), ('/',4)
]

for op, row in operators:
    btn = tk.Button(window, text=op, **btn_params, bg="#FF5722", fg="white", command=lambda t=op: click(t))
    btn.grid(row=row, column=3, padx=5, pady=5, sticky="nsew")

# Clear button
clear_btn = tk.Button(window, text='C', **btn_params, bg="#F44336", fg="white", command=clear)
clear_btn.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

# Make rows and columns expand evenly
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(1,5):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()