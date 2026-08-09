employee = input("Enter Employee's Name: ")


while True:
    productivity_score = int(input("Enter productivity score: "))
    quality_score = int(input("Enter quality score: "))
    attendance_score = int(input("Enter attendance score: "))
    if (
            productivity_score < 0 or productivity_score > 100
            or quality_score < 0 or quality_score > 100
            or attendance_score < 0 or attendance_score > 100
    ):
        print("Enter the Correct score (0-100): ")
    else:
        break

def evaluate_employee(productivity_score, quality_score, attendance_score):

    final_score = productivity_score * 0.40 + quality_score * 0.40 + attendance_score * 0.20
    if final_score >= 90:
        rating = "Excellent"
    elif final_score >= 80:
        rating = "Very Good"
    elif final_score >= 70:
        rating = "Good"
    elif final_score >= 60:
        rating = "Needs Improvement"
    else:
        rating = "Unsatisfactory"
    return final_score, rating

final_score, rating = evaluate_employee(productivity_score, quality_score, attendance_score)

print(f"Employee Name: {employee}")
print(f"Performance Score: {final_score:.2f}")
print(f"Rating: {rating}")


