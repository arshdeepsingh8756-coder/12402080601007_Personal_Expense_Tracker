
import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import date

FILE_NAME = "expenses.json"

# Load saved expenses
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Display all expenses
def show_expenses():
    expense_list.delete(0, tk.END)
    total = 0

    for i, expense in enumerate(expenses):
        text = (
            f"{i + 1}. {expense['name']} | "
            f"Rs. {expense['amount']:.2f} | "
            f"{expense['category']} | {expense['date']}"
        )
        expense_list.insert(tk.END, text)
        total += expense["amount"]

    total_label.config(text=f"Total Expenses: Rs. {total:.2f}")

# Add a new expense
def add_expense():
    name = name_entry.get().strip()
    category = category_entry.get().strip()
    amount_text = amount_entry.get().strip()

    if not name or not category or not amount_text:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        amount = float(amount_text)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid Amount",
            "Enter a valid amount greater than zero."
        )
        return

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    save_expenses()
    show_expenses()

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Expense added successfully!")

# Delete the selected expense
def delete_expense():
    selected = expense_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning", "Please select an expense to delete."
        )
        return

    index = selected[0]
    expenses.pop(index)
    save_expenses()
    show_expenses()

    messagebox.showinfo("Success", "Expense deleted successfully!")

# Main application window
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("750x500")
root.configure(bg="#f0f4f8")

expenses = load_expenses()

# Heading
heading = tk.Label(
    root,
    text="PERSONAL EXPENSE TRACKER",
    font=("Arial", 20, "bold"),
    bg="#f0f4f8",
    fg="#16324f"
)
heading.pack(pady=15)

# Input section
form = tk.Frame(root, bg="#f0f4f8")
form.pack(pady=5)

tk.Label(form, text="Expense Name:", bg="#f0f4f8").grid(
    row=0, column=0, padx=8, pady=8, sticky="w"
)
name_entry = tk.Entry(form, width=25)
name_entry.grid(row=0, column=1, padx=8, pady=8)

tk.Label(form, text="Amount (Rs.):", bg="#f0f4f8").grid(
    row=1, column=0, padx=8, pady=8, sticky="w"
)
amount_entry = tk.Entry(form, width=25)
amount_entry.grid(row=1, column=1, padx=8, pady=8)

tk.Label(form, text="Category:", bg="#f0f4f8").grid(
    row=2, column=0, padx=8, pady=8, sticky="w"
)
category_entry = tk.Entry(form, width=25)
category_entry.grid(row=2, column=1, padx=8, pady=8)

# Buttons
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Expense",
    command=add_expense,
    bg="#287a4b",
    fg="white",
    width=15
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame,
    text="Delete Expense",
    command=delete_expense,
    bg="#c0392b",
    fg="white",
    width=15
).grid(row=0, column=1, padx=8)

# Expense list
expense_list = tk.Listbox(root, width=85, height=10)
expense_list.pack(pady=10)

# Total expenses
total_label = tk.Label(
    root,
    text="Total Expenses: Rs. 0.00",
    font=("Arial", 14, "bold"),
    bg="#f0f4f8",
    fg="#16324f"
)
total_label.pack(pady=10)

# Show previously saved expenses
show_expenses()

root.mainloop()
