student_names  = []
student_scores = []

def add_scores(names, scores, student_name, student_score):
    names.append(student_name)
    scores.append(student_score)

def analyze_scores(scores):
    total = 0
    lowest = scores[0]
    highest = scores[0]

    for score in scores:
        total += score

        if score > highest:
            highest = score
        if score < lowest:
            lowest = score

    average = total / len(scores)

    return total, highest, lowest, average

def find_highest_score(names, scores, highest_score):
    for index, score in enumerate(scores):
        if score == highest_score:
            return names[index]

def find_high_scorers(names, scores):
    high_scorers = []

    for index, score in enumerate(scores):
        if score >= 80:
            high_scorers.append(names[index])

    return high_scorers

while True:
    student_name = input("Enter Student's Name: ")

    while True:
        student_score = float(input("Enter Score: "))

        if student_score < 0 or student_score > 100:
            print("Score must be between 0 and 100. ")
        else:
            break
    add_scores(student_names, student_scores, student_name, student_score)

    while True:
        add_more = input("Do you want to add more data: Yes/ No ").lower()

        if add_more == "yes":
            break
        if add_more == "no":
            break
        else:
            print("Please enter Yes or No.")

    if add_more == "no":
        break

total, highest, lowest, average = analyze_scores(student_scores)

highest_score_name = find_highest_score(student_names, student_scores, highest)
high_scorers = find_high_scorers(student_names, student_scores)

print("\n ---- Student Score Report ---")

for index, student_name in enumerate(student_names):
    print(f"{student_name} : {student_scores[index]}")


print()
print(f"Total Score : {total:.2f}")
print(f"Average Score: {average:.2f}")
print(f"Highest Score: {highest_score_name} - {highest:.2f}")
print(f"Lowest score: {lowest:.2f}")
print(f"Number of students: {len(student_names)}")
print(f"Students scoring 80+: {high_scorers}") 

