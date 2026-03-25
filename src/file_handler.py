import json

def load_expenses():
    with open ("data/expenses.json", "r") as file:
        data = json.load(file)
    return data

def save_expenses(expenses):
    with open ("data/expenses.json", "w") as file:
        json.dump(expenses, file)