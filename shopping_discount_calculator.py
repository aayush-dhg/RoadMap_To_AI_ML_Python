customer_name = input("Enter your name: ")
while True:
    amount = float(input("Enter your total purchase amount: "))
    if amount ==0:
        print("No purchase")
    elif amount < 0:
        print("Invalid amount")
    else:
        break

# $200 or more  → 20% discount
# $100–199.99   → 10% discount
# $50–99.99     → 5% discount
# Below $50     → No discount
def calculate_discount(amount):
    if amount >= 200:
        return amount * 0.20
    elif  amount >= 100:
        return amount * 0.10
    elif amount >= 50:
        return amount * 0.05
    else:
        return 0

discount = calculate_discount(amount)
final_price = amount - discount

print(f"Customer Name: {customer_name}")
print(f"Total Amount: ${amount:.2f}")
print(f"Total Discount: ${discount:.2f}")
print(f"Final Price: ${final_price:.2f}")






