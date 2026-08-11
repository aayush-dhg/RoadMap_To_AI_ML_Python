import random

secret_number = random.randint(1, 20)


def check_guess(secret_number, guess):
    if guess < secret_number:
        return "low"
    elif guess > secret_number:
        return "high"
    else:
        return "correct"

attempts = 0
max_attempts = 5


while attempts < max_attempts:
    print(f"Attempt {attempts+1} of {max_attempts}.") 
    guess = int(input("Guess a number between 1 and 20: "))
    
    if guess < 1 or guess > 20:
        print("Please enter a number between 1 and 20.")
        continue

    attempts += 1
    
    result = check_guess(secret_number, guess)

    if result == "low":
        print("Your guess is too low.")
    elif result == "high":
        print("Your guess is too high.")
    else:
        print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")
        break

else:
    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")

