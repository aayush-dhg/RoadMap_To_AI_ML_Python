import random

students = ["Alex", "Sarah", "Mike", "John", "Emma", "David"]

num = int(input("How many students would you like to pick? "))
while num < 1 or num > len(students):
    print(f"Please enter a number between 1 and {len(students)}.")
    num = int(input("How many students would you like to pick? "))


def pick_unique_students(student_list, num):
    picked_students = []

    while len(picked_students) < num:
        student = random.choice(student_list)
        
        if student not in picked_students:
            picked_students.append(student)
    return picked_students

picked_students = pick_unique_students(students, num)
print(f"The uniquely selected {num} student(s) is/are: {picked_students}")