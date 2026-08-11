text = input("Enter a string to analyze: ").lower()
search_letter = input("Enter a letter to count: ").lower()

while len(search_letter) != 1 or not search_letter.isalpha():
    print("Please enter a single letter.")
    search_letter = input("Enter a letter to count: ").lower()

def count_letter(text, search_letter):
   
    count = 0
    indexes = []
    for index, char in enumerate(text):
        if char == search_letter:
            count += 1
            indexes.append(index)
    return count, indexes

count, indexes = count_letter(text, search_letter)

print(f"The letter '{search_letter}' appears {count} times in the string.")
print(f"Indexes: {indexes} ")