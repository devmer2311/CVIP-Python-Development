import tkinter as tk

def button_click(number):
    current = result_box.get()
    result_box.delete(0, tk.END)
    result_box.insert(0, current + str(number))

def clear():
    result_box.delete(0, tk.END)

def backspace():
    current = result_box.get()
    if current:
        result_box.delete(len(current) - 1)

def evaluate():
    try:
        result = eval(result_box.get())
        result_box.delete(0, tk.END)
        result_box.insert(0, result)
    except Exception:
        result_box.delete(0, tk.END)
        result_box.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

result_box = tk.Entry(root, width=20, borderwidth=5, font=("Arial", 20))
result_box.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', '=', '/',
    'Delete'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=30, pady=30,  font=("Arial", 12), command=evaluate)
    elif button == 'C':
        btn = tk.Button(root, text=button, padx=30, pady=30,  font=("Arial", 12), command=clear)
    elif button == 'Delete':
        btn = tk.Button(root, text=button, padx=120, pady=30,  font=("Arial", 12), command=backspace)
        btn.grid(row=row_val, column=col_val, columnspan=4)
    else:
        btn = tk.Button(root, text=button, padx=30, pady=30,  font=("Arial", 12), command=lambda button=button: button_click(button))

    btn.grid(row=row_val, column=col_val)
    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
