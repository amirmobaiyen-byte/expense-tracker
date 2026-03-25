from expense_manager import add_expense
from file_handler import load_expenses, save_expenses

expenses = load_expenses()

choice = input("1 = add, 2 = view: ") 

if choice == "1":
    add_expense(expenses)
    save_expenses(expenses)

elif choice == "2":
    for item in expenses:
        print(item["name"], "_", item["category"], "_", item["amount"])
