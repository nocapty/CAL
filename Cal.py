import tkinter as tk
from tkinter import messagebox

def click(button_text):
    if button_text == 'C':
        entry.delete(0, tk.END)
    elif button_text == '=':
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width = 20, font = ("Times News Roman", 18), borderwidth = 5, justify = "right")
entry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_val, col_val = 1, 0
for button_text in buttons:
    button = tk.Button(
        root, text = button_text, padx = 20, pady = 20, font = ("Times News Roman", 14),
        command = lambda text = button_text: click(text)
    )

    button.grid(row = row_val, column = col_val, sticky = "nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    root.columnconfigure(i, weight = 1) 
    root.rowconfigure(i, weight = 1)

root.mainloop() 

