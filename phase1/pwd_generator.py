import tkinter as tk
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    if length < 4:
        return "Password length must be at least 4 characters."

    password_list = random.choices(characters, k= length-1)

    if use_uppercase:
        password_list.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password_list.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password_list.append(random.choice(string.digits))
    if use_special_chars:
        password_list.append(random.choice(string.punctuation))

    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

def generate_button_click():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

  

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    result_label.config(text=f"Generated Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root, font=("Times New Roman", 20, "bold"))
length_entry.pack()

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
lowercase_check = tk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var)
special_chars_check = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var)

uppercase_check.pack()
lowercase_check.pack()
digits_check.pack()
special_chars_check.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_button_click, font=("Times New Roman", 24, "bold"))
generate_button.pack()

result_label = tk.Label(root, text="", font=("Times New Roman", 14, "bold"))
result_label.pack(expand=True)

root.mainloop()
