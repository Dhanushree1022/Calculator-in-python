project : Calculator in python                                                                                                                                                                                                                                                    import tkinter as tk
from tkinter import ttk, messagebox

class SimpleCalculator(tk.Tk):
    def _init_(self):
        super()._init_()

        self.title("Simple Calculator")
        self.geometry("340x200")
        self.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # First Number
        tk.Label(self, text="First Number:", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.first_num_var = tk.StringVar()
        self.first_entry = tk.Entry(self, textvariable=self.first_num_var, font=("Arial", 12))
        self.first_entry.grid(row=0, column=1, padx=10, pady=10)

        # Second Number
        tk.Label(self, text="Second Number:", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.second_num_var = tk.StringVar()
        self.second_entry = tk.Entry(self, textvariable=self.second_num_var, font=("Arial", 12))
        self.second_entry.grid(row=1, column=1, padx=10, pady=10)

        # Operation
        tk.Label(self, text="Operation:", bg="#f0f0f0", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.operation_var = tk.StringVar()
        self.operation_var.set("+")  # default
        operations = ["+", "-", "*", "/"]
        self.operation_menu = ttk.Combobox(self, textvariable=self.operation_var, values=operations, font=("Arial", 12), state="readonly", width=5)
        self.operation_menu.grid(row=2, column=1, padx=10, pady=10)

        # Calculate Button
        self.calc_button = tk.Button(self, text="Calculate", command=self.calculate, font=("Arial", 12), bg="#007acc", fg="white")
        self.calc_button.grid(row=3, column=0, columnspan=2, pady=15, ipadx=10, ipady=5)

        # Result Label
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(self, textvariable=self.result_var, bg="#f0f0f0", font=("Arial", 14, "bold"), fg="#333")
        self.result_label.grid(row=4, column=0, columnspan=2)

    def calculate(self):
        try:
            num1 = float(self.first_num_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the first number.")
            self.first_entry.focus_set()
            return
        try:
            num2 = float(self.second_num_var.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the second number.")
            self.second_entry.focus_set()
            return
        
        operation = self.operation_var.get()
        try:
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                result = "Unknown operation"
            self.result_var.set(f"Result: {result}")
        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Division by zero is not allowed.")
            self.result_var.set("")

if _name_ == "_main_":
    app = SimpleCalculator()
    app.mainloop()
