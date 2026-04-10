import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def generate_password():
    if length_entry.get() == placeholder_text:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

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
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, password)

        strength, value = check_strength(password, length)

        strength_var.set(f"Strength: {strength}")
        strength_bar['value'] = value

        if strength == "Weak":
            strength_label.config(fg="red")
        elif strength == "Medium":
            strength_label.config(fg="orange")
        else:
            strength_label.config(fg="green")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def copy_to_clipboard():
    password = result_text.get("1.0", tk.END).strip()

    if password:
        window.clipboard_clear()
        window.clipboard_append(password)

        copy_status_var.set("Copied!")

        window.after(2000, lambda: copy_status_var.set(""))
    else:
        copy_status_var.set("Nothing to copy!")
        window.after(2000, lambda: copy_status_var.set(""))
        
def check_strength(password, length):
    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 1:
        return "Weak", 25
    elif score <= 3:
        return "Medium", 60
    else:
        return "Strong", 100

# Main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("420x420")
window.minsize(420, 380)
strength_bar = ttk.Progressbar(window, length=250, mode='determinate')
strength_bar.pack(pady=5)

include_numbers = tk.BooleanVar(value=True)
include_symbols = tk.BooleanVar(value=True)

strength_var = tk.StringVar()

strength_label = tk.Label(window, textvariable=strength_var)
strength_label.pack()

# Title
title_label = tk.Label(window, text="KeyScribe", font=("Times", 14, "bold"))
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

# Result display (update)
result_var = tk.StringVar()
result_frame = tk.Frame(window)
result_frame.pack(pady=10)

# Text-box
result_text = tk.Text(result_frame, height=3, width=40, wrap="word")
result_text.pack(side="left")

# Scrollbar
scrollbar = tk.Scrollbar(result_frame, command=result_text.yview)
scrollbar.pack(side="right", fill="y")

result_text.config(yscrollcommand=scrollbar.set)

# Copy button
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)
copy_status_var = tk.StringVar()

copy_status_label = tk.Label(window, textvariable=copy_status_var, fg="green")
copy_status_label.pack(pady=5)

# Run app
window.bind("<Return>", lambda event: generate_password())
window.mainloop()
