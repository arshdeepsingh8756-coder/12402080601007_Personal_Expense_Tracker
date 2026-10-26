# 12402080601007_Personal_Expense_Tracker
Personal Expense Tracker

Project Overview

The Personal Expense Tracker is a simple Python-based application that helps users record and manage their daily expenses. It allows users to add expenses, view all recorded expenses, calculate total spending, and delete expenses they no longer need.

The application uses a graphical user interface (GUI) created with Tkinter and saves expense records in a JSON file.

Features

- Add Expense: Enter the expense name, amount, and category.
- View Expenses: Display all saved expenses with their dates.
- Calculate Total: Automatically calculate the total amount spent.
- Delete Expense: Remove a selected expense.
- Save Records: Store expenses in a JSON file for future use.
- Input Validation: Display error messages for missing information or invalid amounts.

Technologies Used

- Programming Language: Python
- GUI Library: Tkinter
- Data Storage: JSON file
- Python Modules: "json", "os", "datetime", "tkinter"

Python Concepts Used

1. Lists: Store multiple expense records.
2. Dictionaries: Store the details of each expense.
3. Functions: Perform operations such as adding, deleting, displaying, and saving expenses.
4. File Handling: Save and load expense records.
5. Exception Handling: Handle invalid amount inputs.
6. GUI Programming: Create an interactive application using Tkinter.

Project Structure

Personal-Expense-Tracker/
│
├── expense_tracker.py
├── expenses.json
└── README.md

Note: The "expenses.json" file is created automatically when the application saves an expense. It may not exist before the first expense is added.

Requirements

- Python 3.x
- Tkinter (usually included with standard Python installations)

No additional third-party libraries are required.

How to Run the Project

Step 1: Download or Clone the Repository

Download the project files or clone the repository to your computer.

Step 2: Open the Project Folder

Open a terminal or command prompt inside the project folder.

Step 3: Run the Python File

Execute the following command:

python expense_tracker.py

If your system uses "python3", run:

python3 expense_tracker.py

Step 4: Use the Application

1. Enter the expense name.
2. Enter the expense amount.
3. Enter the expense category.
4. Click Add Expense.
5. View the expense list and total spending.
6. Select an expense and click Delete Expense to remove it.

Sample Output

Example expense records:

Expense Name| Amount| Category
Lunch| ₹120| Food
Bus Fare| ₹40| Travel
Notebook| ₹80| Education
Total| ₹240| 

The total is calculated automatically based on the recorded expenses.

Advantages

- Easy to use and understand.
- Helps users monitor daily spending.
- Stores expense records for later use.
- Does not require a database server.
- Suitable for Python beginners and academic mini projects.

Limitations

- Expense records are stored locally on the computer.
- The application does not include user login or cloud synchronization.
- It does not generate monthly reports or graphical spending charts.

Future Enhancements

- Add monthly expense reports.
- Include a search and filter feature.
- Display spending charts.
- Add a monthly budget limit.
- Export expense records to CSV.
- Add a user login system.

Conclusion

The Personal Expense Tracker demonstrates the practical use of Python lists, dictionaries, functions, file handling, and Tkinter GUI programming. It provides a simple way to record expenses and calculate total spending while helping students understand the development of a basic desktop application.

Author

Arshdeep Singh

Subject: Programming with Python

Project Title: Personal Expense Tracker
