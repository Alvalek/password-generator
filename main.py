import random
import string
import tkinter as tk
from tkinter import messagebox

include_numbers = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=True)

def generate_password():
    if not include_numbers.get() and not include_symbols.get():
    messagebox.showerror("Error", "Select at least one option (numbers or symbols)!")
    return
    try:
        length = int(length_entry.get())
        characters = string.ascii_letters
            if include_numbers.get():
                characters += string.digits
            if include_symbols.get():
                characters += string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
    if length_entry.get() == placeholder_text:
        messagebox.showerror("Error", "Please enter a valid number!")
    return

def copy_to_clipboard():
    password = result_var.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("320x220")

# Title
title_label = tk.Label(window, text="Password Generator", font=("Arial", 14))
title_label.pack(pady=10)

placeholder_text = "Enter password length..."

def on_entry_click(event):
    if length_entry.get() == placeholder_text:
        length_entry.delete(0, tk.END)
        length_entry.config(fg="black", font=("Arial", 10, "normal"))

def on_focus_out(event):
    if length_entry.get() == "":
        length_entry.insert(0, placeholder_text)
        length_entry.config(fg="gray", font=("Arial", 10, "italic"))

# Length input
length_entry = tk.Entry(window, fg="gray", font=("Arial", 10, "italic"))
length_entry.pack()
length_entry.insert(0, placeholder_text)

length_entry.bind("<FocusIn>", on_entry_click)
length_entry.bind("<FocusOut>", on_focus_out)

numbers_checkbox = tk.Checkbutton(window, text="Include Numbers", variable=include_numbers)
numbers_checkbox.pack()

symbols_checkbox = tk.Checkbutton(window, text="Include Symbols", variable=include_symbols)
symbols_checkbox.pack()

# Generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Result display
result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, wraplength=280)
result_label.pack(pady=10)

# Copy button
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Run app
window.mainloop()
