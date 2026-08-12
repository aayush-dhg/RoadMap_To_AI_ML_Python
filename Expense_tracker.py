expense_names = []
expense_amounts = []

def add_expense(names, amounts, expense_name, expense_amount):
    names.append(expense_name)
    amounts.append(expense_amount)

def analyze_expenses(amounts):
    total = 0
    highest = amounts[0]
    lowest = amounts[0]

    for amount in amounts:
        total += amount

        if amount > highest:
            highest = amount
        if amount < lowest:
            lowest = amount

    average = total / len(amounts)

    return total, highest, lowest, average

def find_highest_expense(names, amounts, highest_amount):
    for index, amount in enumerate(amounts):
        if amount == highest_amount:
            return names[index]

while True:
    expense_name = input("Enter Expense name: ")

    while True:
        expense_amount = float(input("Enter Expense Amount: $"))

        if expense_amount < 0:
            print("Expense amount must be higher than 0.")
        else:
            break

    add_expense(expense_names, expense_amounts, expense_name, expense_amount)

    while True:
        add_more = input("Add another expense? Yes/No : ").lower()

        if add_more == "yes":
            break
        if add_more == "no":
            break
        else:
            print("Please enter Yes or No.")

    if add_more == "no":
        break

total, average, highest, lowest, = analyze_expenses(expense_amounts)

highest_expense_name = find_highest_expense(expense_names, expense_amounts, highest)

print("\n ----Expense Summary----")

for index, expense_name in enumerate(expense_names):
    print(f"{expense_name} : ${expense_amounts[index]:.2f}")

print()
print(f"Total Spending: {total:.2f}")
print(f"Average Expense: {average:.2f}")
print(f"Highest Expense: {highest:.2f}")
print(f"Lowest Expense: {lowest:.2f}")
print(f"Number of Expense: {len(expense_names)}")


    
