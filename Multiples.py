number = int(input("Enter a number: "))
limit = int(input("Enter a limit: "))


def calcultate_multiples(number, limit):
    multiples = []
    total  = 0 
    for i in range(1, limit + 1):
            multiple = number * i
            multiples.append(multiple)
            total += multiple
            
    return multiples, total 

multiples, total  = calcultate_multiples(number, limit)


for i, multiple in enumerate(multiples, start = 1):
    print(f"{number} * {i} = {multiple}")


print(f"The total is: {total}")