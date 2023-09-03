#SIMPLE CALCULATOR
import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(entry_num1.get()) + float(entry_num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def subtract():
    try:
        result.set(float(entry_num1.get()) - float(entry_num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def multiply():
    try:
        result.set(float(entry_num1.get()) * float(entry_num2.get()))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

def divide():
    try:
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
        else:
            result.set(float(entry_num1.get()) / num2)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

add_button = tk.Button(root, text="Add", command=add)
add_button.pack()

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.pack()

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()
