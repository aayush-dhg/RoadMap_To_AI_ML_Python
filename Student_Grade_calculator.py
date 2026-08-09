student_name = input("Enter student's name: ")

while True:

    exam_score = int(input("Enter exam score: "))
    assignment_score = int(input("Enter assignment score: "))
    if exam_score < 0 or assignment_score < 0 or assignment_score > 100 or exam_score > 100:
        print("Invalid input. Enter again,\n")
    else:
        break

def calculate_grade(student, exam_score, assignment_score):
    final_score = (exam_score * 0.60 + assignment_score * 0.40)
    print(f"Student : {student}")
    print("Your final score is: ", final_score, "%")
    if final_score >= 90:
        print(f"Grade: A")
    elif final_score >= 80:
        print(f"Grade: B")
    elif final_score >= 70:
        print(f"Grade: C")
    elif final_score >= 60:
        print(f"Grade: D")
    else:
        print(f"Grade: F")

calculate_grade(student_name, exam_score, assignment_score)



