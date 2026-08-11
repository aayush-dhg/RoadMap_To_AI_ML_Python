text = input("Enter a word or sentence: ").lower()

def analyze_text(text):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    consonant_count = 0
    vowel_list = []
    for char in text:
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)
        elif char.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count, vowel_list


vowel_count, consonant_count, vowel_list = analyze_text(text)
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Vowel letters: {vowel_list}")
print(f"Total letters: {vowel_count + consonant_count}")