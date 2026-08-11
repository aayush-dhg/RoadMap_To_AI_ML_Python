start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))
divisor = int(input("Enter the divisor: "))

while divisor == 0:
    print("Divisor cannot be zero. Please enter a non-zero divisor.")
    divisor = int(input("Enter the divisor: "))

def separate_multiples(start_num, end_num, divisor):
    multiples = []
    total = 0
    count = 0
    largest_multiple = 0
    for num in range(start_num, end_num + 1):
        if num % divisor == 0:
            multiples.append(num)
            total += num
            count += 1
        if num > largest_multiple:
            largest_multiple = num
    return multiples, total, count, largest_multiple

multiples, total, count, largest_multiple = separate_multiples(start_num, end_num, divisor)

print(f"Multiples of {divisor} between {start_num} and {end_num}: {multiples}")
print(f"Total of multiples: {total}")
print(f"Count of multiples: {count}")
print(f"Largest multiple: {largest_multiple}")