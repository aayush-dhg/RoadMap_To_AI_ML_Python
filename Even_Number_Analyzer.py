start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

def analyze_even_numbers(start_num, end_num):
    even_numbers = []
    total_even = 0

    for num in range(start_num, end_num + 1):
        if num % 2 == 0:
            even_numbers.append(num)
            total_even += num

    return even_numbers, total_even

even_numbers, total_even = analyze_even_numbers(start_num, end_num)
print(f"Even numbers between {start_num} and {end_num}: {even_numbers}")
print(f"Total of even numbers: {total_even}")

