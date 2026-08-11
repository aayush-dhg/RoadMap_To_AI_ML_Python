import random
students = ["Alex", "Sarah", "Mike", "John", "Emma", "David"]
num = int(input("Enter the number of students to pick: "))

while num < 1 or num > len(students):
    print(f"Please enter a number between 1 and {len(students)}.")
    num = int(input("Enter the number of students to pick: "))

def pick_random_student(student_list, num):
    return random.sample(student_list, num)

picked_student = pick_random_student(students, num)
print(f"The randomly selected  {num} student is/are: {picked_student}")