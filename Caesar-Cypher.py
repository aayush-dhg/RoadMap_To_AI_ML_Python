# list of alphabets
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    while True:
        direction = input("Type 'encode' to encrypt, 'decode' to decrypt.\n").lower()
        if direction in ["encode", "decode"]:
            break
        else:
            print("Invalid input. Please type 'encode' or 'decode'.\n")

    text = input("Type your message: \n").lower()


    while True:
        shift_input = input("Type the shift number: \n")

        if shift_input.isdigit():
            shift = int(shift_input)
            break
        else:
            print("Invalid input. Please enter a number.\n")


    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    while True:
        restart = input("Type 'Yes' if you want to go again. Otherwise type 'No'.\n").lower()
        if restart == 'no':
            should_continue = False
            print("Good Bye")
            break
        elif restart == "yes":
            break
        else:
            print("Invalid input. Please Type 'Yes' or 'No'.\n")



    