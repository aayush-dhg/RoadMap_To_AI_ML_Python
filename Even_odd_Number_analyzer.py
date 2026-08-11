start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

def separate_numbers(start_num, end_num):
    even_numbers = []
    odd_numbers = []
    total_even = 0
    total_odd = 0

    for num in range(start_num, end_num + 1):
        if num % 2 == 0:
            even_numbers.append(num)
            total_even += num
        if num % 2 != 0:
            odd_numbers.append(num)
            total_odd += num
    if total_even > total_odd:
        even_check = True
    if total_odd > total_even: 
        even_check = False
    if total_even == total_odd:
        even_check = None
    return even_numbers, odd_numbers, total_even, total_odd, even_check

even_numbers, odd_numbers, total_even, total_odd, even_check = separate_numbers(start_num, end_num)

print(f"Even numbers between {start_num} and {end_num}: {even_numbers}")
print(f"Odd numbers between {start_num} and {end_num}: {odd_numbers}")
print(f"Total of even numbers: {total_even}")
print(f"Total of odd numbers: {total_odd}")

if even_check is True:
    print(f"The total of even numbers is greater than the total of odd numbers.")
elif even_check is False:
    print(f"The total of odd numbers is greater than the total of even numbers.")
if even_check is None:
    print(f"The totals of even and odd numbers are equal.")
