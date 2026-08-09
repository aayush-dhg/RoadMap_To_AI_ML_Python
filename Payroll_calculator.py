# Exercise 1 — Employee Pay Calculator
#
# Imagine you're building a small payroll utility for a company.
#
# Write a Python program that asks the user for:
#
# Employee name
# Number of hours worked this week
# Hourly pay rate
#
# Then calculate the employee's weekly pay.
#
# There is one important rule:
#
# If the employee works more than 40 hours, every hour above 40 is paid at 1.5× the normal hourly rate.

print("Payroll Software")

employee = input("Enter employee name: ")

while True:

    hours = int(input("Enter hours: "))
    hourly_rate = int(input("Enter hourly rate: "))
    if hours < 0 or hourly_rate < 0:
        print("Invalid input. Enter again,\n")
    else:
        break

def  payroll(employee, hours, hourly_rate):
    if hours <= 40:
        regular_pay = hourly_rate * hours
        extra_hours = 0
        print(f"Total hours worked: {hours}\n"
              f"Weekly pay: {regular_pay}\n"
              f"Extra hours: {extra_hours}")
    else:
        extra_hours = hours - 40
        extra_pay = extra_hours * hourly_rate * 1.5
        regular_pay = (40 * hourly_rate) + extra_pay
        print(f"Total hours worked: {hours}\n"
              f"Weekly pay: {regular_pay}\n"
              f"Extra hours: {extra_hours}\n"
              f"Extra pay: {extra_pay}")


payroll(employee, hours, hourly_rate)


