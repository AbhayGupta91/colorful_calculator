# task 3
import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        messagebox.showerror("Error", "Cannot divide by zero.")
        return "Error"
    return x / y

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        result_label.config(text=f"Result: {result}", bd=2, relief="groove")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def clear_entries():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="Result: ", bd=0)

def on_hover(e):
    e.widget.config(bg="#40E0D0", fg="white")

def on_leave(e):
    e.widget.config(bg="lightblue", fg="black")

root = tk.Tk()
root.title("Creative Modern Calculator")
root.geometry("360x520")
root.config(bg="lightgray")

operation_var = tk.StringVar(root)
operation_var.set("+")

label_num1 = tk.Label(root, text="Enter the first number:", font=("Arial", 12), bg="lightgray")
label_num1.pack(pady=5)

entry_num1 = tk.Entry(root, font=("Arial", 12))
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter the second number:", font=("Arial", 12), bg="lightgray")
label_num2.pack(pady=5)

entry_num2 = tk.Entry(root, font=("Arial", 12))
entry_num2.pack(pady=5)

label_operation = tk.Label(root, text="Choose an operation:", font=("Arial", 12), bg="lightgray")
label_operation.pack(pady=5)

option_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
option_menu.config(font=("Arial", 12))
option_menu.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=("Arial", 14, "bold"), bg="lightblue", fg="black")
calculate_button.pack(pady=15)
calculate_button.bind("<Enter>", on_hover)
calculate_button.bind("<Leave>", on_leave)

result_label = tk.Label(root, text="Result: ", font=("Arial", 16, "bold"), bg="lightgray")
result_label.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_entries, font=("Arial", 14, "bold"), bg="orange", fg="white")
clear_button.pack(pady=5)
clear_button.bind("<Enter>", on_hover)
clear_button.bind("<Leave>", on_leave)

# Customizing the appearance of arithmetic operation buttons
operation_buttons_frame = tk.Frame(root, bg="lightgray")
operation_buttons_frame.pack(pady=5)

def select_operation(op):
    operation_var.set(op)

operation_buttons = [
    ("+", "+"),
    ("-", "-"),
    ("*", "×"),
    ("/", "÷"),
]

for op, symbol in operation_buttons:
    button = tk.Button(operation_buttons_frame, text=symbol, command=lambda op=op: select_operation(op), font=("Arial", 14, "bold"), width=6, height=2)
    button.grid(row=0, column=operation_buttons.index((op, symbol)), padx=5, pady=5)
    button.bind("<Enter>", on_hover)
    button.bind("<Leave>", on_leave)

# "Made by: Abhay Gupta" text
made_by_label = tk.Label(root, text="Made by: Abhay Gupta", font=("Arial", 10), fg="gray", bg="lightgray")
made_by_label.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
