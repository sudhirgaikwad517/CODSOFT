import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error (Divide by zero)"

        result_label.config(text="Result: " + str(result))

    except ValueError:
        result_label.config(text="Error (Invalid input)")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widgets for input numbers
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Label for result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=0, column=2, padx=10, pady=10)

# Dropdown for selecting operation
operations = ['+', '-', '*', '/']
operation_var = tk.StringVar()
operation_var.set(operations[0])  # Default operation
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=1, column=0, padx=10, pady=10)

# Button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=1, padx=10, pady=10)

# Run the GUI
root.mainloop()
