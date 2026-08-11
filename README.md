# 🐍 Python Practice Journey

Welcome to my Python learning repository.

This repository contains hands-on exercises I am completing while strengthening my Python fundamentals and problem-solving skills. Instead of only following tutorials, I am building small programs that gradually introduce new concepts and improve in difficulty over time.

The goal is to develop a strong Python foundation before progressing into more advanced programming, automation, data science, machine learning, and Generative AI.

---

## 🚀 What I'm Practicing

Through these exercises, I am working on:

* Variables and data types
* User input with `input()`
* Type conversion using `int()` and `float()`
* Arithmetic operators
* Conditional statements

  * `if`
  * `elif`
  * `else`
* Logical operators

  * `and`
  * `or`
* Input validation
* `while` loops
* `break`
* Functions
* Function parameters
* Returning values with `return`
* Multiple return values
* Formatted strings / f-strings
* Writing cleaner and more reusable code
* Problem-solving and debugging

---

# 📚 Exercises

## Exercise 1 — Employee Pay Calculator

A payroll calculator that determines an employee's weekly pay.

### Features

* Accepts employee name, hours worked, and hourly rate
* Calculates regular pay
* Calculates overtime pay for hours above 40
* Overtime is paid at `1.5x` the normal hourly rate
* Rejects negative hours and pay rates
* Uses a `while` loop to request valid input again
* Uses a function with parameters

### Concepts Practiced

```python
input()
if/ elif / else
while True
break
functions
parameters
logical operators
```

---

## Exercise 2 — Student Grade Calculator

Calculates a student's final grade using weighted exam and assignment scores.

### Weighting

```text
Exam Score       = 60%
Assignment Score = 40%
```

### Grade Scale

| Final Score | Grade |
| ----------- | ----- |
| 90–100      | A     |
| 80–89.99    | B     |
| 70–79.99    | C     |
| 60–69.99    | D     |
| Below 60    | F     |

### Features

* Validates scores between `0` and `100`
* Continues asking until valid values are entered
* Calculates a weighted final score
* Assigns the appropriate letter grade
* Uses function parameters

### Important Lesson

Instead of checking ranges like:

```python
80 <= score <= 89
```

I learned to simplify descending conditions:

```python
if score >= 90:
    ...
elif score >= 80:
    ...
elif score >= 70:
    ...
```

This also correctly handles decimal values such as `89.4`.

---

## Exercise 3 — Shopping Cart Discount Calculator

Calculates a customer's discount based on their purchase amount.

### Discount Rules

| Purchase Amount | Discount    |
| --------------- | ----------- |
| $200+           | 20%         |
| $100–199.99     | 10%         |
| $50–99.99       | 5%          |
| Below $50       | No Discount |

### Features

* Validates purchase amount
* Calculates discount using a function
* Introduces the `return` statement
* Uses the returned value outside the function
* Calculates the final purchase price

### Key Concept

```python
discount = calculate_discount(amount)

final_price = amount - discount
```

This exercise helped me understand the difference between:

```python
print()
```

and:

```python
return
```

A function can calculate a value and return it so that another part of the program can use it.

---

## Exercise 4 — Restaurant Bill Calculator

Calculates a restaurant bill including tip and tax.

### Features

* Accepts meal cost
* Accepts tip percentage
* Validates user input
* Calculates tip
* Calculates tax
* Calculates the final bill
* Uses multiple functions together

### Functions

```python
calculate_tip()
calculate_total()
calc_tax()
```

One function can return a value that is then used in another calculation.

Example:

```python
tip = calculate_tip(meal_cost, tip_percentage)

total = calculate_total(meal_cost, tip)
```

This exercise introduced the idea of breaking a larger problem into smaller reusable functions.

---

## Exercise 5 — Employee Performance Evaluator

Evaluates employee performance using three weighted scores.

### Weighting

```text
Productivity = 40%
Quality      = 40%
Attendance   = 20%
```

### Performance Ratings

| Score    | Rating            |
| -------- | ----------------- |
| 90+      | Excellent         |
| 80+      | Very Good         |
| 70+      | Good              |
| 60+      | Needs Improvement |
| Below 60 | Unsatisfactory    |

### Features

* Validates all scores between `0` and `100`
* Calculates a weighted performance score
* Assigns a performance rating
* Returns multiple values from one function

### Key Concept

```python
return final_score, rating
```

The returned values can then be unpacked:

```python
final_score, rating = evaluate_employee(
    productivity_score,
    quality_score,
    attendance_score
)
```

This was my introduction to returning multiple values from a function.

---

# 🧠 Key Lessons So Far

### Validating a Range

Valid:

```python
0 <= score <= 100
```

Invalid:

```python
score < 0 or score > 100
```

---

### Repeating Until Valid Input

```python
while True:
    value = int(input("Enter value: "))

    if value < 0:
        print("Invalid input")
    else:
        break
```

---

### Functions with Parameters

```python
def calculate_total(price, tax):
    return price + tax
```

---

### Returning a Value

```python
def calculate_discount(amount):
    return amount * 0.20
```

Then:

```python
discount = calculate_discount(amount)
```

---

### Returning Multiple Values

```python
def calculate_result(score):
    return score, "Excellent"
```

Then:

```python
score, rating = calculate_result(score)
```

---

# 🛠️ Technologies

![Python](https://img.shields.io/badge/Python-Learning-blue?logo=python\&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-IDE-green?logo=pycharm)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)

---

# 🎯 Learning Roadmap

```text
Python Fundamentals
        ↓
Functions
        ↓
Loops & Validation
        ↓
Lists / Dictionaries
        ↓
More Complex Programs
        ↓
Object-Oriented Programming
        ↓
APIs & Automation
        ↓
Data Processing
        ↓
Machine Learning
        ↓
Generative AI
```

---

# 📈 Progress

* [x] Exercise 1 — Employee Pay Calculator
* [x] Exercise 2 — Student Grade Calculator
* [x] Exercise 3 — Shopping Cart Discount Calculator
* [x] Exercise 4 — Restaurant Bill Calculator
* [x] Exercise 5 — Employee Performance Evaluator
* [ ] Exercise 6 — Coming Next
* [ ] More exercises to come...

---

# 💡 Purpose of This Repository

This repository is not intended to contain perfect code from day one.

It documents the process of:

> **Write → Test → Find mistakes → Understand why → Fix → Improve**

Each exercise is designed to introduce a small new concept while reinforcing concepts learned previously.

The objective is not simply to memorize Python syntax, but to develop the ability to break a problem into logical steps and translate those steps into working code.

---

## 🌱 Current Status

Currently strengthening **Python fundamentals** with progressively harder programming exercises.

Next up:

> **Exercise 6 — Lists + Functions**

Exercise 6 focused on strengthening one of the most important beginner Python combinations:

```text
Lists + Functions + Loops
```

Instead of working with single values, these exercises introduced passing entire lists into functions, processing items one by one, and returning useful results.

---

### Exercise 6A — Search for an Item

Created a function that checks whether a user-entered item exists in a shopping list.

Example list:

```python
shopping_list = ["apple", "milk", "bread", "banana", "cheese"]
```

The user can search for an item:

```text
Enter item to search: banana
```

Output:

```text
banana is in the shopping list.
```

If the item does not exist:

```text
Enter item to search: chicken
```

Output:

```text
chicken is not in the shopping list.
```

### Key Concepts Practiced

```python
if search_item in shopping_list:
```

* Passing a list into a function
* Passing multiple parameters
* Using the `in` operator
* Returning `True` or `False`
* Using a returned Boolean value outside the function

Example:

```python
def analyzing_list(shopping_list, search_item):
    if search_item in shopping_list:
        return True
    else:
        return False
```

A simplified version can also be written as:

```python
def analyzing_list(shopping_list, search_item):
    return search_item in shopping_list
```

---

### Exercise 6B — Count Matching Items

Extended the previous exercise by counting how many times an item appears in a list.

Example list:

```python
shopping_list = [
    "apple",
    "milk",
    "bread",
    "banana",
    "cheese",
    "apple",
    "milk"
]
```

Example:

```text
Enter item to search: apple
```

Output:

```text
apple appears 2 times.
```

If the item appears once:

```text
cheese appears 1 time.
```

If it does not appear:

```text
chicken is not in the shopping list.
```

### Key Concepts Practiced

* Looping through a list
* Comparing each list item
* Using a counter variable
* Incrementing with `+=`
* Returning a count from a function
* Using the returned count with `if / elif / else`

Core logic:

```python
def analyzing_list(shopping_list, search_item):
    count = 0

    for item in shopping_list:
        if item == search_item:
            count += 1

    return count
```

This exercise reinforced an important pattern:

```text
Start counter at 0
        ↓
Loop through list
        ↓
Check each item
        ↓
Increase counter when matched
        ↓
Return final count
```

---

### Exercise 6C — Build and Return a New List

Created a function that filters items from an existing list and returns a new list.

The goal was to find all shopping-list items containing more than 5 letters.

Example:

```python
shopping_list = [
    "apple",
    "milk",
    "bread",
    "banana",
    "cheese",
    "avocado",
    "mango"
]
```

Expected result:

```python
["banana", "cheese", "avocado"]
```

### Key Concepts Practiced

* Creating an empty list
* Looping through an existing list
* Using `len()` on strings
* Filtering with an `if` condition
* Adding values using `.append()`
* Returning an entire list from a function
* Understanding local variables inside functions

Core logic:

```python
def find_long_items(shopping_list):
    new_shopping_list = []

    for item in shopping_list:
        if len(item) > 5:
            new_shopping_list.append(item)

    return new_shopping_list
```

This introduced another important programming pattern:

```text
Original List
      ↓
Function
      ↓
Create Empty List
      ↓
Loop Through Original List
      ↓
Check Condition
      ↓
Append Matching Items
      ↓
Return New List
```

---

### What I Learned from Exercise 6

These exercises helped strengthen the relationship between lists and functions.

The three main patterns were:

```text
6A → Check whether something exists in a list

6B → Count how many times something appears

6C → Filter items and create a new list
```

I also improved my understanding of the difference between:

```python
for item in shopping_list:
```

which processes individual items, and:

```python
len(shopping_list)
```

or:

```python
search_item in shopping_list
```

which operate on the list as a whole.

Exercise 6 was especially useful for understanding how functions can receive a list, process its contents, and return different types of results such as:

```text
Boolean → True / False
Integer → count
List → filtered results
```

## Exercise 7 — For Loops + Lists + Data Analysis

Exercise 7 focused on analyzing numerical data manually using loops instead of relying on built-in shortcuts such as:

```python
max()
min()
sum()
```

The goal was to understand how these operations work internally.

---

### Exercise 7 — Score Analyzer

Analyzed a list of student scores and calculated:

* Highest score
* Lowest score
* Average score

Example:

```python
scores = [78, 92, 65, 88, 100, 54, 81]
```

Core logic:

```python
highest = scores[0]
lowest = scores[0]
total = 0

for score in scores:
    total += score

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score
```

### Key Concepts Practiced

* Initializing variables from the first list element
* Accumulators
* Manual highest-value search
* Manual lowest-value search
* Calculating averages
* Multiple return values

---

### Exercise 7A — Temperature Analyzer

Reinforced the same pattern using temperature data.

```python
temperatures = [72, 85, 68, 91, 77, 64, 88]
```

The function calculated:

```text
Highest Temperature
Lowest Temperature
Average Temperature
```

This exercise strengthened the pattern:

```text
initialize
    ↓
loop
    ↓
compare
    ↓
update
    ↓
calculate
    ↓
return
```

---

### Exercise 7B — Sales Analyzer

Expanded the analysis by performing multiple operations during the same loop.

The function calculated:

* Highest sale
* Lowest sale
* Average sale
* Number of sales above $200

Example:

```python
sales = [120, 250, 90, 300, 175, 80, 260]
```

A counter was introduced:

```python
above_200 = 0

for sale in sales:
    if sale > 200:
        above_200 += 1
```

This showed how one loop can perform several independent analyses efficiently.

---

### Exercise 7C — Filter Sales Into a New List

Combined numerical analysis with list filtering.

The program created a new list containing only sales greater than `$200`.

Example:

```python
sales = [120, 250, 90, 300, 175, 80, 260]
```

Filtered result:

```python
[250, 300, 260]
```

Core logic:

```python
def filter_sales(sales):
    filtered_sales = []

    for sale in sales:
        if sale > 200:
            filtered_sales.append(sale)

    return filtered_sales
```

Additional functions were created to calculate:

* Total of filtered sales
* Highest filtered sale

### Key Learning

One function's returned list can be passed into another function:

```text
Original List
     ↓
filter_sales()
     ↓
Filtered List
     ↓
 ┌──────────────┐
 ↓              ↓
total_sales()  find_highest()
```

---

# Exercise 8 — `range()` + Loops + Calculations

Exercise 8 focused on understanding Python's `range()` function and using generated number sequences inside loops.

---

### Exercise 8 — Multiplication Table Generator

Created a function that generated multiplication results up to a user-defined limit.

Example:

```text
Number: 5
Limit: 5
```

Output:

```text
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
```

The program also calculated the total of all products.

Core concept:

```python
for i in range(1, limit + 1):
```

This reinforced that the ending value in `range()` is excluded.

For example:

```python
range(1, 6)
```

produces:

```text
1, 2, 3, 4, 5
```

---

### Exercise 8A — Even Number Analyzer

Used `range()` and the modulo operator `%` to find even numbers.

Example:

```text
Start: 1
End: 10
```

Result:

```python
[2, 4, 6, 8, 10]
```

Core condition:

```python
if num % 2 == 0:
```

The function returned:

* List of even numbers
* Total of even numbers

---

### Exercise 8B — Separate Even and Odd Numbers

Expanded Exercise 8A by creating two lists during the same loop.

```python
even_numbers = []
odd_numbers = []
```

Each number was classified using:

```python
if num % 2 == 0:
    ...
else:
    ...
```

The program calculated:

* Even-number list
* Odd-number list
* Total of even numbers
* Total of odd numbers

It also compared the totals.

A three-state result was introduced:

```python
True
False
None
```

where:

```text
True  → even total is greater
False → odd total is greater
None  → totals are equal
```

This was also an introduction to using:

```python
is None
```

---

### Exercise 8C — Multiples Analyzer

Created a program that finds numbers divisible by a user-provided divisor.

Example:

```text
Start: 1
End: 30
Divisor: 5
```

Result:

```python
[5, 10, 15, 20, 25, 30]
```

The function calculated:

* Matching multiples
* Total of multiples
* Number of matches
* Largest matching multiple

Core condition:

```python
if num % divisor == 0:
```

Input validation was also added to prevent:

```python
divisor = 0
```

because modulo by zero is invalid.

### Key Concepts Practiced

```text
range()
%
.append()
counters
accumulators
input validation
manual maximum search
multiple return values
```

---

# Exercise 9 — Random Module + Lists

Exercise 9 introduced Python's `random` module and explored several ways of making random selections.

---

### Exercise 9 — Random Student Picker

Used:

```python
random.sample()
```

to randomly select multiple unique students from a list.

Example:

```python
students = ["Alex", "Sarah", "Mike", "John", "Emma", "David"]
```

Core function:

```python
def pick_random_student(student_list, num):
    return random.sample(student_list, num)
```

Validation ensured that:

```text
1 <= number selected <= total students
```

---

### Exercise 9A — Unique Random Selection Using `random.choice()`

Recreated the behavior of `random.sample()` manually using:

```python
random.choice()
```

A `while` loop repeatedly selected students.

Duplicates were prevented with:

```python
if student not in picked_students:
```

Core logic:

```python
while len(picked_students) < num:
    student = random.choice(student_list)

    if student not in picked_students:
        picked_students.append(student)
```

### Important Difference Learned

```text
random.choice()
→ selects one random item
→ duplicates are possible

random.sample()
→ selects multiple unique items
→ no duplicates
```

---

### Exercise 9B — Number Guessing Game

Used:

```python
random.randint(1, 20)
```

to generate a secret number.

The player received a limited number of attempts to guess correctly.

A separate function evaluated each guess:

```python
def check_guess(secret_number, guess):
    if guess < secret_number:
        return "low"
    elif guess > secret_number:
        return "high"
    else:
        return "correct"
```

The game loop handled:

* Attempt counting
* Invalid guesses
* Correct guesses
* Maximum attempts
* `break`
* `continue`

### Important Lesson

The program separated responsibilities:

```text
check_guess()
→ evaluates the guess

while loop
→ controls the game
```

This helped reinforce writing smaller functions with clearly defined responsibilities.

---

# Exercise 10 — Nested Conditions + Login System

Exercise 10 focused on nested `if` statements.

A simple login system was created with:

```python
correct_username = "admin"
correct_password = "password123"
```

The login-checking function used nested conditions:

```python
def check_login(username, password):
    if username == correct_username:
        if password == correct_password:
            return "Login successful"
        else:
            return "Incorrect password"
    else:
        return "Incorrect username"
```

The program allowed a maximum of three login attempts.

### Key Concepts Practiced

* Nested `if`
* Authentication-style logic
* Attempt counters
* `while` loops
* `break`
* Functions
* Return values

### Logic Flow

```text
Username correct?
      ↓ yes
Password correct?
   ↓ yes      ↓ no
Success     Wrong password

Username incorrect
      ↓
Wrong username
```

---

# Exercise 11 — String Analysis

Exercise 11 introduced more detailed string processing using loops.

---

### Exercise 11 — Vowel and Consonant Analyzer

The user entered a word or sentence.

The function analyzed every character and returned:

* Number of vowels
* Number of consonants
* List of vowels found

Core loop:

```python
for char in text:
    if char in vowels:
        vowel_count += 1
        vowel_list.append(char)

    elif char.isalpha():
        consonant_count += 1
```

### New String Method

```python
.isalpha()
```

was used to determine whether a character is alphabetic.

Examples:

```python
"a".isalpha()   # True
"7".isalpha()   # False
" ".isalpha()   # False
"!".isalpha()   # False
```

This allowed spaces, numbers, and punctuation to be ignored when counting consonants.

---

### Exercise 11A — Letter Counter + Index Finder

Created a program that asks the user for:

* A word or sentence
* A letter to search for

The program manually counted occurrences without using:

```python
.count()
```

Input validation ensured that the search input contained exactly one alphabetic character:

```python
while len(search_letter) != 1 or not search_letter.isalpha():
```

The function then used:

```python
enumerate()
```

to retrieve both the index and character while looping.

Example:

```python
for index, char in enumerate(text):
```

For:

```text
banana
```

Python processes:

```text
Index 0 → b
Index 1 → a
Index 2 → n
Index 3 → a
Index 4 → n
Index 5 → a
```

Matching indexes were stored using:

```python
indexes.append(index)
```

Example result:

```text
Search letter: a

Count: 3
Indexes: [1, 3, 5]
```

### Key Concept

The difference between:

```python
for char in text:
```

and:

```python
for index, char in enumerate(text):
```

is that `enumerate()` provides both:

```text
index + value
```

---

# 🧠 Major Concepts Reinforced in Exercises 7–11

These exercises significantly expanded the earlier fundamentals.

### Lists and Loops

```text
Iterating through lists
Filtering lists
Building new lists
Counters
Accumulators
Comparing values
```

### Functions

```text
Parameters
Return values
Multiple return values
Passing returned data into another function
Separating responsibilities between functions
```

### Number Processing

```text
range()
modulo %
even / odd checks
divisibility
manual maximum
manual minimum
averages
```

### Randomization

```python
random.choice()
random.sample()
random.randint()
```

### Loop Control

```python
break
continue
```

### Strings

```python
.isalpha()
.lower()
len()
enumerate()
```

### Membership Checks

```python
in
not in
```

---

# 📈 Updated Progress

* [x] Exercise 1 — Employee Pay Calculator
* [x] Exercise 2 — Student Grade Calculator
* [x] Exercise 3 — Shopping Cart Discount Calculator
* [x] Exercise 4 — Restaurant Bill Calculator
* [x] Exercise 5 — Employee Performance Evaluator
* [x] Exercise 6A — List Membership Search
* [x] Exercise 6B — Duplicate Counter
* [x] Exercise 6C — List Filtering
* [x] Exercise 7 — Score Analyzer
* [x] Exercise 7A — Temperature Analyzer
* [x] Exercise 7B — Sales Analyzer
* [x] Exercise 7C — Sales Filtering
* [x] Exercise 8 — Multiplication Table
* [x] Exercise 8A — Even Number Analyzer
* [x] Exercise 8B — Even/Odd Separator
* [x] Exercise 8C — Multiples Analyzer
* [x] Exercise 9 — Random Student Picker
* [x] Exercise 9A — Unique Random Picker
* [x] Exercise 9B — Number Guessing Game
* [x] Exercise 10 — Login Attempt System
* [x] Exercise 11 — String Analyzer
* [x] Exercise 11A — Letter Count & Index Finder
* [ ] Exercise 12 — Next
* [ ] Final Fundamentals Mini Project

---

## 🚀 Current Skill Progress

At this stage, I am becoming more comfortable combining multiple Python concepts instead of practicing them independently.

The exercises are increasingly following this pattern:

```text
Input
  ↓
Validation
  ↓
Function
  ↓
Loop
  ↓
Conditional Logic
  ↓
List / String Processing
  ↓
Return Result
  ↓
Output
```

The focus remains on understanding how Python works manually before relying on built-in shortcuts.

The next exercises will continue reinforcing these fundamentals before moving toward larger Python projects and more advanced topics.


These patterns are foundational for more advanced Python, data processing, automation, and machine learning.


⭐ This repository will continue to grow as I progress through Python and eventually move toward Machine Learning and Generative AI.
