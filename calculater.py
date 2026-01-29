import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            # eval() calculates the string expression
            result = eval(current_text)
            enter.delete(0, tk.END)
            enter.insert(tk.END, str(result))
        except zeroDivisionError:
            messagebox .showerror("Error","Cannot divide by zero")
            enter.delete(0, tk.END)
        except Exception:
           messagebox.showerror("Error","invalid Input")
           enter.delete(0, tk.END)
    elif button_text == "C":
           enter.delete(0, tk.END)
    else:

           entry.insert(tk.END, button_text)
        
