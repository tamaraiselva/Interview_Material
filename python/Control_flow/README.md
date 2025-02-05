# **CONTROL FLOW**

- [If-Else Statements](#if-else-statements)

- [While and For Loops](#while-and-for-loops)

- [Break Continue Pass Statements](#break-continue-pass-statements)

# If-Else-Statements

1. **What is an if-else statement? Explain its syntax in Python?**
   - An if-else statement allows a program to execute certain code blocks based on whether a condition is `True` or `False`. 

**Syntax in Python:**

```python
if condition:
    # code block if condition is True
else:
    # code block if condition is False
```
<br>

**Example:**
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

---

2. **What is the difference between `if`, `elif`, and `else` in Python?**
   - `if`: The first condition to check.
   - `elif`: Short for "else if", used to check multiple conditions sequentially after the initial `if`.
   - `else`: The default block that executes if none of the `if` or `elif` conditions are `True`.

**Example:**
```python
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print(grade)  # Output: B
```

---

3. **What is the purpose of the elif statement in Python?**
   - The `elif` statement stands for "else if." It allows you to check multiple conditions sequentially. If the condition for the if statement is false, the elif condition is checked. If the elif condition is also false, the else block (if present) is executed.

---

4. **How would you handle multiple conditions using if-else statements?**
   - You can handle multiple conditions using a combination of `if`, `elif`, and `else` statements:

**Syntax in Python:**

   ```python
   if condition1:
       # code to execute if condition1 is true
   elif condition2:
       # code to execute if condition1 is false and condition2 is true
   elif condition3:
       # code to execute if condition1 and condition2 are false and condition3 is true
   else:
       # code to execute if none of the above conditions are true
   ```

**Example:**
```python
num = 0
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
elif num < 0:
    print("Negative")
```

---

5. **Explain nested if statements with an example?**
   - Nested if statements are `if` statements within another `if` or `else` block. They allow for more complex condition checking.

**Syntax in Python:**

```python
   if condition1:
       if condition2:
           # code if condition1 and condition2 are true
       else:
           # code if condition1 is true and condition2 is false
   else:
       # code if condition1 is false
   ```

**Example:**
```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")
```

---
   
6. **How can you use conditional expressions (ternary operators) in Python?**
   - Conditional expressions allow you to write a concise if-else statement on a single line:

   ```python
   result = value_if_true if condition else value_if_false
   ```

---

7. **What is the difference between elif and else in Python?**
   `elif` (short for else if) allows you to check multiple conditions in sequence. If the condition for the if statement is false, it checks the condition of the first elif block. If that is also false, it checks the next elif block, and so on. `else` is used to execute a block of code if none of the previous conditions are true.

---

8. **Can you have an if statement without an else or elif?**
   - Yes, an if statement can stand alone without an else or elif. In such cases, if the condition is false, no code block is executed.

---

9 **How does short-circuit evaluation work in Python’s if statements?**
  - In Python, logical operators (`and`, `or`) use short-circuit evaluation. This means that in an `and` operation, if the first condition is `False`, the second condition is not evaluated. Similarly, in an `or` operation, if the first condition is `True`, the second condition is not evaluated.

**Example:**
```python
def check():
    print("Checking...")
    return True

if False and check():
    print("This won't print.")
# Output: Nothing, as `check()` is not called.

if True or check():
    print("This prints without calling `check()`.")
# Output: This prints without "Checking..."
```

---
<br>

# Coding Questions

### 1. **Check Divisibility by Multiple Numbers**

**Question:**  
Write a Python program that takes an integer as input and checks if it is divisible by both 3 and 5, only by 3, only by 5, or by neither.

**Solution:**
```python
def check_divisibility(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Divisible by both 3 and 5"
    elif n % 3 == 0:
        return "Divisible by 3"
    elif n % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not divisible by 3 or 5"

# Example Usage
print(check_divisibility(15))  # Output: Divisible by both 3 and 5
print(check_divisibility(9))   # Output: Divisible by 3
print(check_divisibility(10))  # Output: Divisible by 5
print(check_divisibility(7))   # Output: Not divisible by 3 or 5
```

---

### 2. **Simple Calculator**

**Question:**  
Write a Python program that functions as a simple calculator. It should take two numbers and an operator (`+`, `-`, `*`, `/`) as input and perform the corresponding arithmetic operation.

**Solution:**
```python
def simple_calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"

# Example Usage
print(simple_calculator(10, 5, '+'))  # Output: 15
print(simple_calculator(10, 5, '-'))  # Output: 5
print(simple_calculator(10, 5, '*'))  # Output: 50
print(simple_calculator(10, 0, '/'))  # Output: Error: Division by zero
print(simple_calculator(10, 5, '^'))  # Output: Invalid operator
```

---

### 3. **Check for Prime Number**

**Question:** Write a program that checks if a number is prime.

**Answer:**
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(29))  # Output: True
print(is_prime(30))  # Output: False
```

---

### 4. **Check if a Number is Even or Odd**

**Question:** Write a program to determine if a number is even or odd.

**Solution:**
```python
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
print(check_even_odd(10))  # Output: Even
print(check_even_odd(5))   # Output: Odd
```

---

### 5. **Check for Vowel or Consonant**

**Question:** Write a program that checks if a character is a vowel or consonant.

**Solution:**
```python
def check_vowel(character):
    vowels = "aeiouAEIOU"
    if character in vowels:
        return "Vowel"
    else:
        return "Consonant"

# Example usage
print(check_vowel('a'))  # Output: Vowel
print(check_vowel('b'))  # Output: Consonant
```

---

### 6. **Check if a Year is a Leap Year**

**Question:** Write a program that checks if a given year is a leap year.

**Solution:**
```python
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Example usage
print(is_leap_year(2020))  # Output: Leap Year
print(is_leap_year(2021))  # Output: Not a Leap Year
```

---

### 7. **Determine the Sign of a Number**

**Question:** Write a program that checks if a number is positive, negative, or zero.

**Solution:**
```python
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage
print(check_number(5))   # Output: Positive
print(check_number(-3))  # Output: Negative
print(check_number(0))   # Output: Zero
```

---

### 8. **Day of the Week**

**Question:** Write a program that prints the name of the day based on a number (1-7).

**Solution:**
```python
def day_of_week(day):
    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "Invalid day"

# Example usage
print(day_of_week(3))  # Output: Wednesday
```

---

### 9. **Number Classification**

**Question:** Write a program that classifies a number as "small" (1-10), "medium" (11-20), or "large" (21 and above).

**Solution:**
```python
def classify_number(num):
    if 1 <= num <= 10:
        return "Small"
    elif 11 <= num <= 20:
        return "Medium"
    else:
        return "Large"

# Example usage
print(classify_number(5))   # Output: Small
print(classify_number(15))  # Output: Medium
print(classify_number(25))  # Output: Large
```

---

### 10. **Grade Classification with Multiple Conditions**

**Question:**  
Enhance the grade classification program to include distinctions for plus and minus grades based on the exact score. For example:
- 90-100: A
  - 90-92: A-
  - 93-96: A
  - 97-100: A+
- Similarly for other grades (B, C, D)

**Solution:**
```python
def detailed_grade(marks):
    if marks >= 90:
        if marks <= 92:
            return 'A-'
        elif marks <= 96:
            return 'A'
        else:
            return 'A+'
    elif marks >= 80:
        if marks <= 82:
            return 'B-'
        elif marks <= 86:
            return 'B'
        else:
            return 'B+'
    elif marks >= 70:
        if marks <= 72:
            return 'C-'
        elif marks <= 76:
            return 'C'
        else:
            return 'C+'
    elif marks >= 60:
        if marks <= 62:
            return 'D-'
        elif marks <= 66:
            return 'D'
        else:
            return 'D+'
    else:
        return 'F'

# Example Usage
print(detailed_grade(91))  # Output: A-
print(detailed_grade(95))  # Output: A
print(detailed_grade(98))  # Output: A+
print(detailed_grade(85))  # Output: B
print(detailed_grade(73))  # Output: C-
print(detailed_grade(65))  # Output: D
print(detailed_grade(55))  # Output: F
```

---

### 11. **Identify the Type of a Triangle Based on Angles**

**Question:**  
Write a Python program that takes three angles of a triangle as input and determines if the triangle is:
- **Acute**: All angles are less than 90 degrees
- **Right**: One angle is exactly 90 degrees
- **Obtuse**: One angle is greater than 90 degrees
- **Invalid**: If the angles do not sum up to 180 degrees

**Solution:**
```python
def triangle_angle_type(angle1, angle2, angle3):
    total = angle1 + angle2 + angle3
    if total != 180:
        return "Invalid Triangle"
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "Right Triangle"
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        return "Obtuse Triangle"
    else:
        return "Acute Triangle"

# Example Usage
print(triangle_angle_type(60, 60, 60))  # Output: Acute Triangle
print(triangle_angle_type(90, 45, 45))  # Output: Right Triangle
print(triangle_angle_type(100, 40, 40)) # Output: Obtuse Triangle
print(triangle_angle_type(50, 60, 80))  # Output: Invalid Triangle
```

---

### 12. **Find the Second Largest Number in a List**

**Question:**  
Write a Python program to find the second largest number in a list of integers.

**Solution:**
```python
def second_largest(numbers):
    if len(numbers) < 2:
        return "List does not have enough elements."
    first, second = (numbers[0], float('-inf'))
    for num in numbers[1:]:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else "No second largest element."

# Example Usage
print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
print(second_largest([10, 10, 10]))         # Output: No second largest element.
print(second_largest([5]))                  # Output: List does not have enough elements.
```

---


# While-and-For_Loops

1. **Explain the difference between `for` and `while` loops in Python?**
   - **For Loop:** Iterates over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. It is typically used when the number of iterations is known or finite.

   - **While Loop:** Repeats as long as a given condition is `True`. It is used when the number of iterations is not known beforehand and depends on dynamic conditions.

```python
# While loop example
while condition:
    # code to execute while condition is true

# For loop example
for item in sequence:
    # code to execute for each item in sequence
```

**Example For Loop:**
```python
for i in range(5):
    print(i)
# Outputs: 0 1 2 3 4
```

**Example While Loop:**
```python
i = 0
while i < 5:
    print(i)
    i += 1
# Outputs: 0 1 2 3 4
```

---

2. **How do you iterate over a dictionary using a for loop? Provide an example.**
   - You can iterate over a dictionary’s keys, values, or key-value pairs using the `.keys()`, `.values()`, or `.items()` methods respectively.

**Example:**
```python
student_grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}

# Iterate over keys
for student in student_grades:
    print(student)

# Iterate over values
for grade in student_grades.values():
    print(grade)

# Iterate over key-value pairs
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
```

---

3. **How does the `range()` function work in Python’s for loops?**
   - The `range()` function generates a sequence of numbers, which is commonly used to specify the number of iterations in a `for` loop.

**Syntax:**
- `range(stop)`: Generates numbers from 0 to stop-1.
- `range(start, stop)`: Generates numbers from start to stop-1.
- `range(start, stop, step)`: Generates numbers from start to stop-1, incremented by step.

**Example:**
```python
for i in range(3):
    print(i)
# Outputs: 0 1 2

for i in range(1, 4):
    print(i)
# Outputs: 1 2 3

for i in range(0, 10, 2):
    print(i)
# Outputs: 0 2 4 6 8
```

---

4. **What is an infinite loop? How can it be avoided or broken?**
   - An infinite loop is a loop that never terminates because the terminating condition is never met or there's no terminating condition.

**Avoidance:**
- Ensure that the loop has a condition that eventually becomes `False`.
- Update variables involved in the loop condition appropriately within the loop.

**Breaking an Infinite Loop:**
- Use `break` to exit the loop based on a condition.
- Include a termination condition that can be met.

**Example Avoiding Infinite Loop:**
```python
i = 0
while i < 5:
    print(i)
    i += 1  # Ensures the loop will terminate
```

---

5. **Can you modify the loop variable inside a for loop? What are the implications?**
   - Yes, you can modify the loop variable inside a `for` loop, but it does not affect the iteration sequence.

**Example:**
```python
for i in range(5):
    print(i)
    i += 10  # Modifies the loop variable
# Outputs: 0 1 2 3 4

**Implications:**
- Modifying the loop variable does not change the sequence generated by `range()`.
- It can lead to confusion and is generally discouraged unless necessary for specific logic.

```

6. **What are the potential risks of using a while loop?**
   - A major risk is creating an infinite loop if the condition never becomes false. This can cause the program to hang or crash.

---

7. **Can you use else with loops in Python?**
   - Yes, both while and for loops can have an else clause in Python. The else block is executed after the loop completes normally (i.e., it is not terminated by a break statement).

---

8. **What is the purpose of the enumerate() function in a for loop?**
   - The `enumerate()` function adds a counter to an iterable and returns it as an enumerate object, which can be used to obtain both the index and the value in a loop:

   ```python
   my_list = ['a', 'b', 'c']
   for index, value in enumerate(my_list):
       print(index, value)
   ```

---
<br>

# Coding Questions

Here are some of the most commonly asked interview questions related to **`while`** and **`for`** loops:

### 1. Sum of Natural Numbers
**Question:** Write a program that calculates the sum of the first `n` natural numbers using a loop.

**Answer:**
```python
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage
print(sum_natural_numbers(5))  # Output: 15
```

---

### 2. Factorial of a Number
**Question:** Write a program that computes the factorial of a number using a loop.

**Answer:**
```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
print(factorial(5))  # Output: 120
```

---

### 3. Fibonacci Sequence
**Question:** Write a program to print the Fibonacci sequence up to `n` terms using a loop.

**Answer:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage
fibonacci(5)  # Output: 0 1 1 2 3
```

---

### 4. Reverse a Number
**Question:** Write a program that reverses a given integer using a loop.

**Answer:**
```python
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

# Example usage
print(reverse_number(12345))  # Output: 54321
```

---

### 5. Count Vowels in a String
**Question:** Write a program that counts the number of vowels in a given string using a loop.

**Answer:**
```python
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Example usage
print(count_vowels("Hello World"))  # Output: 3
```

---

### 6. Multiplication Table
**Question:** Write a program that prints the multiplication table of a given number using a loop.

**Answer:**
```python
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage
multiplication_table(5)
```

---

### 7. Find Largest Element in a List
**Question:** Write a program that finds the largest element in a list using a loop.

**Answer:**
```python
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage
print(find_largest([1, 3, 5, 7, 9]))  # Output: 9
```

---

### 8. Print Prime Numbers within a Range
**Question:** Write a program that prints all prime numbers between `1` and `n` using a loop.

**Answer:**
```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(n):
    for num in range(1, n + 1):
        if is_prime(num):
            print(num, end=' ')

# Example usage
print_primes(20)  # Output: 2 3 5 7 11 13 17 19
```

---

### 9. Count Digits in a Number
**Question:** Write a program that counts the number of digits in a given integer using a loop.

**Answer:**
```python
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

# Example usage
print(count_digits(12345))  # Output: 5
```

---

### 10. Remove Duplicates from a List
**Question:** Write a program that removes duplicate elements from a list using a loop.

**Answer:**
```python
def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Example usage
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

---

### 11. Print a Pattern
**Question:** Write a program to print a right-angled triangle pattern of stars based on the input number of rows.

**Answer:**
```python
def print_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

# Example usage
print_triangle(5)
```
**Output:**
```
*
**
***
****
*****
```

---

### 12. Check Palindrome
**Question:** Write a program to check if a given string is a palindrome using a loop.

**Answer:**
```python
def is_palindrome(s):
    s = s.lower()
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return s == reversed_s

# Example usage
print(is_palindrome("Radar"))  # Output: True
print(is_palindrome("Hello"))  # Output: False
```

---

### 13. Sum of Digits
**Question:** Write a program that calculates the sum of the digits of a given integer using a loop.

**Answer:**
```python
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# Example usage
print(sum_of_digits(12345))  # Output: 15
```

---

### 14. Generate a List of Squares
**Question:** Write a program to generate a list of squares of numbers from `1` to `n` using a loop.

**Answer:**
```python
def generate_squares(n):
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return squares

# Example usage
print(generate_squares(5))  # Output: [1, 4, 9, 16, 25]
```

---

### 15. Count Consonants in a String
**Question:** Write a program that counts the number of consonants in a given string using a loop.

**Answer:**
```python
def count_consonants(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# Example usage
print(count_consonants("Hello World"))  # Output: 7
```

---

### 16. Find GCD (Greatest Common Divisor)
**Question:** Write a program that calculates the GCD of two numbers using a loop.

**Answer:**
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
print(gcd(48, 18))  # Output: 6
```

---

### 17. Check Armstrong Number
**Question:** Write a program to check if a number is an Armstrong number using a loop.

**Answer:**
```python
def is_armstrong(num):
    total = 0
    order = len(str(num))
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    return total == num

# Example usage
print(is_armstrong(153))  # Output: True
print(is_armstrong(123))  # Output: False
```

---

### 18. Reverse a String
**Question:** Write a program that reverses a given string using a loop.

**Answer:**
```python
def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

# Example usage
print(reverse_string("Hello"))  # Output: "olleH"
```

---

### 19. Calculate Exponential
**Question:** Write a program that calculates `x` raised to the power of `n` using a loop.

**Answer:**
```python
def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

# Example usage
print(power(2, 3))  # Output: 8
```

---

### 20. Print Odd Numbers in a Range

**Question:** Write a program to print all odd numbers between `1` and `n` using a loop.

**Answer:**

```python
def print_odd_numbers(n):
    for i in range(1, n + 1, 2):
        print(i, end=' ')

# Example usage
print_odd_numbers(10)  # Output: 1 3 5 7 9
```

---
<br>

##  Break-Continue-Pass-Statements

1. **What does the `break` statement do in a loop? Provide an example.**
   - The `break` statement exits the nearest enclosing loop immediately, skipping any remaining iterations.

**Example:**

```python
for num in range(10):
    if num == 5:
        break
    print(num)
# Outputs: 0 1 2 3 4
```

---

2. **How does the `continue` statement work in loops? Give an example.**
   - The `continue` statement skips the current iteration and proceeds to the next iteration of the loop.

**Example:**
```python
for num in range(5):
    if num == 2:
        continue
    print(num)
# Outputs: 0 1 3 4
```

---

3. **What is the purpose of the `pass` statement in Python? When would you use it?**
   - The `pass` statement is a no-operation placeholder used when a statement is syntactically required but no action is needed. It’s often used during development as a placeholder for future code.

**Example:**
```python
def function_that_does_nothing():
    pass

for num in range(5):
    if num == 3:
        pass  # Placeholder for future code
    print(num)
# Outputs: 0 1 2 3 4
```

---

4. **Can `break` and `continue` be used in nested loops? Explain with an example.**
   - Yes, `break` and `continue` affect only the nearest enclosing loop.

**Example:**
```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Exits the inner loop
        print(f"i={i}, j={j}")
# Outputs:
# i=0, j=0
# i=1, j=0
# i=2, j=0

for i in range(3):
    for j in range(3):
        if j == 1:
            continue  # Skips to the next iteration of the inner loop
        print(f"i={i}, j={j}")
# Outputs:
# i=0, j=0
# i=0, j=2
# i=1, j=0
# i=1, j=2
# i=2, j=0
# i=2, j=2
```

---

5. **Is it possible to exit multiple nested loops at once? If not, how can you achieve this?**
   - Python does not support directly breaking out of multiple nested loops. To achieve this, you can use flags, exceptions, or refactor the code into functions.

**Using a Flag:**
```python
found = False
for i in range(5):
    for j in range(5):
        if some_condition(i, j):
            found = True
            break
    if found:
        break
```

**Using Exceptions:**
```python
class BreakOutLoop(Exception):
    pass

try:
    for i in range(5):
        for j in range(5):
            if some_condition(i, j):
                raise BreakOutLoop
except BreakOutLoop:
    pass
```

**Using Functions:**
```python
def search():
    for i in range(5):
        for j in range(5):
            if some_condition(i, j):
                return (i, j)
    return None

result = search()
```

---

6. **What is the difference between break and return statements in loops?**
   - The `break` statement exits the innermost loop, while the `return` statement exits the entire function and returns a value (if specified).

---

# Coding Questions

Here are some commonly asked interview questions focusing on the **`break`**, **`continue`**, and **`pass`** statements in Python


### 1. Use `break` to Exit a Loop
**Question:** Write a program that prints numbers from `1` to `10`, but stops when it reaches `6` using the `break` statement.

**Answer:**
```python
def print_numbers():
    for i in range(1, 11):
        if i == 6:
            break
        print(i)

# Example usage
print_numbers()  # Output: 1 2 3 4 5
```

---

### 2. Use `continue` to Skip an Iteration
**Question:** Write a program that prints even numbers from `1` to `10`, skipping the odd numbers using the `continue` statement.

**Answer:**
```python
def print_even_numbers():
    for i in range(1, 11):
        if i % 2 != 0:
            continue
        print(i)

# Example usage
print_even_numbers()  # Output: 2 4 6 8 10
```

---

### 3. Use `pass` in a Loop
**Question:** Write a program that prints numbers from `1` to `10`. Use `pass` for the odd numbers and print a message for even numbers.

**Answer:**
```python
def print_numbers_with_pass():
    for i in range(1, 11):
        if i % 2 != 0:
            pass  # Do nothing for odd numbers
        else:
            print(f"{i} is even")

# Example usage
print_numbers_with_pass()  # Output: 2 is even, 4 is even, 6 is even, 8 is even, 10 is even
```

---

### 4. Find First Prime Number
**Question:** Write a program that finds and prints the first prime number greater than `10` and less than `50`, using `break`.

**Answer:**
```python
def first_prime():
    for num in range(11, 50):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:  # This else corresponds to the for loop, not the if statement
            print(num)
            break

# Example usage
first_prime()  # Output: 11
```

---

### 5. Skip Specific Values
**Question:** Write a program that prints numbers from `1` to `20`, but skips `5` and `10` using the `continue` statement.

**Answer:**
```python
def skip_specific_values():
    for i in range(1, 21):
        if i == 5 or i == 10:
            continue
        print(i)

# Example usage
skip_specific_values()  # Output: 1 2 3 4 6 7 8 9 11 12 13 14 15 16 17 18 19 20
```

---

### 6. Using `pass` for Future Implementation
**Question:** Write a program that checks if a number is positive, negative, or zero. Use `pass` to handle the "zero" case for future implementation.

**Answer:**
```python
def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        pass  # Future implementation for zero case

# Example usage
check_number(0)  # No output, but can be implemented later
```

---


### 7. Count Until a Condition
**Question:** Write a program that counts numbers from `1` to `20`, but stops counting when it reaches `15` using the `break` statement.

**Answer:**
```python
def count_until():
    count = 0
    for i in range(1, 21):
        if i == 15:
            break
        count += 1
    return count

# Example usage
print(count_until())  # Output: 14
```

---

### 8. Use `continue` to Filter Values
**Question:** Write a program that filters out and prints all numbers greater than `5` from a list of numbers using the `continue` statement.

**Answer:**
```python
def filter_numbers(numbers):
    for num in numbers:
        if num <= 5:
            continue
        print(num)

# Example usage
filter_numbers([1, 3, 5, 7, 9, 2, 6])  # Output: 7 9 6
```

---

### 9. Nested Loops with `break`
**Question:** Write a program that finds the first odd number in a nested loop, where the outer loop goes from `1` to `5` and the inner loop goes from `1` to `10`.

**Answer:**
```python
def find_first_odd():
    for i in range(1, 6):
        for j in range(1, 11):
            if j % 2 != 0:
                print(f"First odd number: {j}")
                break
        break  # Exiting the outer loop after the first odd number is found

# Example usage
find_first_odd()  # Output: First odd number: 1
```

---

### 10. Counting Down
**Question:** Write a program that counts down from `10` to `1`, using `break` to stop if it reaches `5`.

**Answer:**
```python
def countdown():
    for i in range(10, 0, -1):
        if i == 5:
            break
        print(i)

# Example usage
countdown()  # Output: 10 9 8 7 6
```

---

### 11. Skip Negative Numbers
**Question:** Write a program that takes a list of numbers and prints only the positive numbers, using continue to skip the negatives.

**Answer:**

```python
def print_positive_numbers(numbers):
    for num in numbers:
        if num < 0:
            continue
        print(num)

# Example usage
print_positive_numbers([-1, 2, -3, 4, -5, 6])  # Output: 2 4 6
```


