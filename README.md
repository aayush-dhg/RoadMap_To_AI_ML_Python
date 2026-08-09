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
if / elif / else
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

---

⭐ This repository will continue to grow as I progress through Python and eventually move toward Machine Learning and Generative AI.
