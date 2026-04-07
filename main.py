import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

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

# Length input
length_entry = tk.Entry(window)
length_entry.pack()
length_entry.insert(0, "12")

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
