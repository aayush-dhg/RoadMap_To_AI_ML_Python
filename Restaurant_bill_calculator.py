customer_name = input("Enter your name: ")

while True:

    meal_cost = float(input("Enter your meal cost: "))
    tip_percentage = float(input("Enter your tip percentage: "))
    if meal_cost  <= 0:
        print("Invalid Meal Cost! Enter again \n")
    elif 0 >= tip_percentage:
        print("Invalid! \n")
    else:
        break

def calculate_tip(meal_cost, tip_percentage):
    return  meal_cost * tip_percentage / 100

def calculate_total(meal_cost, tip_amount):
    return meal_cost + tip_amount
def calc_tax(meal_cost):
    return meal_cost * 0.0825


tip = float(calculate_tip(meal_cost, tip_percentage))
total = float(calculate_total(meal_cost, tip))


tax = float(calc_tax(meal_cost))
final_price =  total + tax

print(f"Customer Name: {customer_name}")
print(f"Meal Cost: ${meal_cost:.2f}")
print(f"Tip Percentage: {tip_percentage:.2f}%")
print(f"Tip Amount: ${tip:.2f}")
print(f"Total Amount: ${total:.2f}")
print(f"Tax Amount: ${tax:.2f}")
print(f"FinalAmount: ${final_price:.2f}")








