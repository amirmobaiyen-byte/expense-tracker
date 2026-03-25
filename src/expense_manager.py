def add_expense(expenses):
    # we have the varables here when they ask the user to stored the data
    name = input("Namana Soxdun?")
    category = input("O nmn de got?")
    amount = float(input("Necha Girde?"))

    # now here awe have the dictionary 
    item = {
        "name" : name,
        "category" : category,
        "amount" : amount,
        }
    expenses.append(item)