import random
import string
import tkinter as tk
from tkinter import ttk


def generate_password():
    """Generate a random password based on user-selected length and options."""
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        password_output.set("Invalid length! Please enter a positive number.")
        return

    # Build the character pool
    character_pool = ""
    if use_lowercase.get():
        character_pool += string.ascii_lowercase
    if use_uppercase.get():
        character_pool += string.ascii_uppercase
    if use_numbers.get():
        character_pool += string.digits
    if use_symbols.get():
        character_pool += string.punctuation

    if not character_pool:
        password_output.set("Please select at least one character type.")
        return

    # Generate the password
    password = "".join(random.choice(character_pool) for _ in range(length))
    password_output.set(password)


def copy_to_clipboard():
    """Copy the generated password to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(password_output.get())
    root.update()
    copied_label.config(text="Copied to clipboard!")


# Initialize the main GUI window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")
root.configure(bg="#f0f8ff")

# Title Label
title_label = tk.Label(
    root,
    text="🔒 Random Password Generator",
    font=("Arial", 18, "bold"),
    bg="#f0f8ff",
    fg="#1e3d59",
)
title_label.pack(pady=10)

# Password Length Input
length_frame = tk.Frame(root, bg="#f0f8ff")
length_frame.pack(pady=10)
length_label = tk.Label(
    length_frame,
    text="Password Length:",
    font=("Arial", 12),
    bg="#f0f8ff",
    fg="#333333",
)
length_label.pack(side=tk.LEFT, padx=5)
length_var = tk.StringVar(value="8")
length_entry = ttk.Entry(length_frame, textvariable=length_var, width=10)
length_entry.pack(side=tk.LEFT, padx=5)

# Character Options
options_frame = tk.Frame(root, bg="#f0f8ff")
options_frame.pack(pady=10)
use_lowercase = tk.BooleanVar(value=True)
use_uppercase = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(
    options_frame, text="Lowercase", variable=use_lowercase, bg="#f0f8ff"
).grid(row=0, column=0, padx=10, sticky="w")
tk.Checkbutton(
    options_frame, text="Uppercase", variable=use_uppercase, bg="#f0f8ff"
).grid(row=0, column=1, padx=10, sticky="w")
tk.Checkbutton(options_frame, text="Numbers", variable=use_numbers, bg="#f0f8ff").grid(
    row=1, column=0, padx=10, sticky="w"
)
tk.Checkbutton(options_frame, text="Symbols", variable=use_symbols, bg="#f0f8ff").grid(
    row=1, column=1, padx=10, sticky="w"
)

# Generate Button
generate_button = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12, "bold"),
    bg="#0073e6",
    fg="white",
    relief="flat",
)
generate_button.pack(pady=20)

# Password Output
password_output = tk.StringVar(value="Your password will appear here.")
password_label = tk.Label(
    root,
    textvariable=password_output,
    wraplength=350,
    font=("Arial", 14, "bold"),
    bg="#f0f8ff",
    fg="#333333",
)
password_label.pack(pady=10)

# Copy Button and Copied Label
copy_frame = tk.Frame(root, bg="#f0f8ff")
copy_frame.pack(pady=10)

copy_button = tk.Button(
    copy_frame,
    text="📋 Copy Password",
    command=copy_to_clipboard,
    font=("Arial", 12),
    bg="#4caf50",
    fg="white",
    relief="flat",
)
copy_button.pack(side=tk.LEFT, padx=5)

copied_label = tk.Label(
    copy_frame, text="", font=("Arial", 10), bg="#f0f8ff", fg="#333333"
)
copied_label.pack(side=tk.LEFT, padx=5)

# Footer
footer_label = tk.Label(
    root,
    text="🔑 Generate strong passwords effortlessly!",
    font=("Arial", 10),
    bg="#f0f8ff",
    fg="#555555",
)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Start the main loop
root.mainloop()
