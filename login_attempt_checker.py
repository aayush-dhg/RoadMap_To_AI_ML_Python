correct_username = "admin"
correct_password = "password123"

def check_login(username, password):
    if username == correct_username:
        if password == correct_password:
            return "Login successful"
        else:
            return "Incorrect password"
    else:
        return "Incorrect username"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Attempt {attempts + 1} of {max_attempts}.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    result = check_login(username, password)

    if result == "Login successful":
        print(result)
        break
    else:
        print(result)
        attempts += 1
else:
    print("Maximum login attempts exceeded.")

