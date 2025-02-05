# Interview Questions on Functions 

**1. What is a function in programming?**

**Ans:**  A function is a reusable block of code that performs a specific task. It can take input parameters, process them, and return an output. Functions help in organizing code, promoting reusability, and improving readability.


**2.How do you define a function in Python?**

**Ans:** You define a function in Python using the `def` keyword followed by the function name and a set of parentheses containing parameters.

- Syntax:

```python
def my_function(parameter1, parameter2):
# Function body
# ...
```

- Example: 

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

In this example, the `greet` function takes a parameter `name` and returns a greeting message. The function is called with the argument `"Alice"`, resulting in the output "Hello, Alice!".

---

**3. How do you call a function in Python?**

**Ans:** You call a function by using its name followed by parentheses containing arguments (if any). For example, my_function(arg1, arg2).

- Example:

```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # Calling the greet function with an argument
```


**4. What is the difference between parameter and argument in python function?**

**Ans:**   In Python, the terms **parameter** and **argument** are often used interchangeably, but they refer to different concepts in the context of functions:

**Parameter**

A **parameter** is a variable in the function definition that acts as a placeholder. It defines what kind of input the function expects when it is called. Parameters exist only in the function signature, and they are used within the function to refer to the values passed to it.

- Example:

```python
def greet(name):
    return f"Hello, {name}!"
```
In this example, `name` is a **parameter**. It's the placeholder for the value that will be provided when the function is called.

**Argument**

An **argument** is the actual value that you pass to the function when calling it. Arguments fill the placeholders (parameters) and provide the data for the function to work with.

- Example:

```python
greet("Alice")
```

Here, `"Alice"` is an **argument**. It's the actual value provided to the `greet` function to replace the `name` parameter.

- Key Differences:

| Feature      | Parameter                                   | Argument                                     |
|--------------|---------------------------------------------|----------------------------------------------|
| **Definition**| A variable in the function definition that defines what the function expects | The actual value passed to the function when calling it |
| **Location** | Declared in the function signature (definition) | Passed in the function call (invocation)     |
| **Purpose**  | Acts as a placeholder for the argument       | Provides the actual data to be processed     |

- Example :

```python
def add(a, b):  # 'a' and 'b' are parameters
    return a + b

result = add(5, 3)  # 5 and 3 are arguments
```

- `a` and `b` are **parameters** because they define what values are expected when `add` is called.

- `5` and `3` are **arguments** because they are the actual values passed into the function when calling it (`add(5, 3)`).

- **Parameters** are used in the function definition to define what the function expects.

- **Arguments** are the actual values passed to the function when it is called.


**5. What is a function signature in Python?**

**Ans:**  A function signature consists of the function name and the number and types of its parameters. It helps identify the function.


**6. What is a docstring, and why is it used in Python functions?**

**Ans:** A docstring is a string literal used to provide documentation for functions, classes, or modules. It helps users understand the purpose and usage of the function.

```python
def my_function(parameter):
"""
This is a docstring.
It provides documentation for the function.
"""
# Function body
# ...

```

**7. What are the advantages of using functions?**

**Ans:**  

- **Modularity:** Functions break code into manageable sections.

- **Reusability:** Functions can be reused across different parts of the program.

- **Maintainability:** Code is easier to maintain and debug.

- **Abstraction:** Functions hide complex logic behind simple function calls.

- Example: 

```python
def calculate_area(radius):
    return 3.14 * radius * radius

# Reusing the function
area1 = calculate_area(5)
area2 = calculate_area(10)
print(area1, area2)  # Output: 78.5 314.0
```

   
Here, the `calculate_area` function computes the area of a circle given its radius. This function can be reused to calculate the area for different radii without rewriting the logic.

---

**8. What is a higher-order function?**

**Ans:** A higher-order function is a function that takes one or more functions as arguments or returns a function as a result. They are commonly used for operations like map, filter, and reduce in functional programming.

- Example: 
```python
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

result = apply_function(square, 5)
print(result)  # Output: 25
```

   
The `apply_function` takes another function `func` and a value, applies the function to the value, and returns the result. In this case, `square` is passed as the function to be applied.

---

**9. Explain the concept of recursion. Provide an example.**

**Ans:**  
Recursion is a programming technique where a function calls itself to solve a problem. It typically has a base case to stop the recursion and a recursive case to continue the process.

- Example: 

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

The `factorial` function calculates the factorial of a number `n`. The base case is when `n` is 0, returning 1. For other values, the function calls itself with `n - 1`, multiplying the result with `n`.

---

**10. What are default parameters in functions?**

**Ans:**  Default parameters allow a function to have predefined values for parameters if no argument is passed during the function call. 

- Example: 

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())          # Output: Hello, Guest!  , greet()  # Calling greet with the default parameter value
print(greet("Alice"))  # Output: Hello, Alice!   , greet("Alice")  # Calling greet with a specified argument
```
   
In the `greet` function, the parameter `name` has a default value of "Guest". If no argument is provided during the call, this default value is used.

---

**11. What is the purpose of the `return` statement in a function?**

**Ans:**  The `return` statement is used to exit a function and send a value back to the caller. If no `return` statement is present, the function returns `None` by default in Python.

- Example: 

```python
def add(a, b):
    return a + b

result = add(2, 3)  # result will be 5
print(result)       # Output: 5
```
 
The `add` function takes two parameters, `a` and `b`, and returns their sum. The value returned is stored in the variable `result`.

---

**12. Explain the concept of *args and **kwargs in Python.**

**Ans:**  
- `*args`: Allows a function to accept a variable number of positional arguments. It is treated as a tuple within the function.
  
- `**kwargs`: Allows a function to accept a variable number of keyword arguments. It is treated as a dictionary within the function.

- Example: 

```python
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}
```

In this example, `my_function` accepts any number of positional and keyword arguments. The positional arguments are captured in a tuple, and keyword arguments in a dictionary.

---

**13. What is variable scope in Python functions, and how does it work?**

**Ans:**  Variable scope defines where a variable is accessible. In Python, variables defined within a function have local scope, while variables defined outside functions have global scope.

- Example:

```python
# Global variable
message = "Hello from the global scope!"

def greet():
    # Local variable
    message = "Hello from the local scope!"
    print(message)  # This will print the local variable

# Calling the function
greet()

# Accessing the global variable outside the function
print(message)  # This will print the global variable


#Output:

Hello from the local scope!
Hello from the global scope!
```

**14. What is the difference between `return` and `print` in a function?**

**Ans:**  

- `return`: Sends a value back to the caller of the function and terminates the function. It allows the value to be stored in a variable for further use.
  
- `print`: Displays a value to the console but does not return it to the caller. It is used for debugging or output purposes.

- Example:

```python
def add(a, b):
    return a + b  # returns the sum

def print_add(a, b):
    print(a + b)  # prints the sum

result = add(2, 3)      # result will be 5
print_add(2, 3)         # Output: 5
```
  
In this example, `add` returns the sum of two numbers, which can be stored or used later, while `print_add` simply prints the result to the console without returning it.

---

**15. What is function overloading?**

**Ans:**  Function overloading allows multiple functions to have the same name with different parameters. It is commonly found in languages like Java or C++. In Python, you can achieve similar functionality using default arguments or variable-length arguments, as it does not support traditional overloading.

- Example: 

```python
def add(a, b, c=0):
    return a + b + c

print(add(2, 3))      # Output: 5


print(add(2, 3, 4))   # Output: 9
```
  
Here, the `add` function can take either two or three parameters. If the third parameter is not provided, it defaults to 0.

---

**16. What are anonymous functions (lambda functions)?**

**Ans:**  Anonymous functions, or lambda functions, are small, unnamed functions defined with the `lambda` keyword. They can take any number of arguments but can only have one expression.

- Example: 

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

Here, `add` is assigned a lambda function that takes two arguments and returns their sum. This function can be called just like a regular function.

---

**17. How do you handle exceptions in a function?**

**Ans:**  Exceptions can be handled using the `try` and `except` blocks within a function. This allows for graceful error handling without crashing the program.

- Example:

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Cannot divide by zero
```

In the `divide` function, an attempt is made to divide `a` by `b`. If `b` is zero, a `ZeroDivisionError` is caught, and a friendly message is returned instead of crashing the program.

---

**18. What is a pure function?**

**Ans:**  A pure function is a function that:

- Always produces the same output for the same input.

- Does not cause any side effects (such as modifying global variables or changing input arguments).

- Example: 

```python
def add(a, b):
    return a + b  # Pure function

print(add(2, 3))  # Output: 5
```
   
The `add` function is pure because it returns the same result for the same inputs and does not alter any external state.

---

**19. How do you define a function within another function?**

**Ans:**  A function can be defined inside another function, which is known as a nested function. The inner function can access variables from the enclosing (outer) function.

- Example: 

```python
def outer_function(x):
    def inner_function(y):
        return y + x
    return inner_function

result = outer_function(5)(3)
print(result)  # Output: 8
```

In this example, `inner_function` is defined inside `outer_function` and uses `x` from the outer scope. The inner function is returned and then called with an argument.

---

**20. What is the use of the `global` keyword?**

**Ans:**  The `global` keyword is used to modify a variable outside the current scope. It allows you to change a global variable inside a function.

- Example: 
```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```
 
In this example, the `count` variable is declared as global inside the `increment` function, allowing the function to modify its value, which persists outside the function.

---

**21. Explain the difference between mutable and immutable objects in relation to functions.**

**Ans:** 

- **Mutable objects** (like lists and dictionaries) can be modified after creation. If passed to a function, changes made to the object inside the function affect the original object.
  
- **Immutable objects** (like tuples and strings) cannot be changed. If passed to a function, a new object is created instead of modifying the original.

- Example: 

```python
def modify_list(lst):
    lst.append(4)  # Modifies the original list

def modify_string(s):
    s += " world"  # Creates a new string

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

my_string = "Hello"
modify_string(my_string)
print(my_string)  # Output: Hello
```
   
In this example, `modify_list` alters the original list, while `modify_string` does not affect `my_string`, as strings are immutable.

---

**22. What is the purpose of function annotations?**

**Ans:**  
Function annotations provide a way to attach metadata to function parameters and return values. They are primarily used for type hints, helping with code readability and static analysis.

- Example: 

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))  # Output: 5
```

In this example, `a` and `b` are annotated as integers, and the return type is also annotated as an integer. This helps developers understand what types of arguments are expected.

---

**23. How do you create a function that returns another function?**

**Ans:**  

You can define a function that returns another function as a result. This is useful for creating closures.

- Example: 

```python
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
print(double(5))  # Output: 10
```
   
Here, `multiplier` returns a new function `multiply`, which multiplies its input by the `factor` specified. The returned function can be assigned to a variable (`double`) and used later.

---

**24. What are named and positional arguments?**

**Ans:** 

- **Positional arguments** are passed to a function in the order defined.
  
- **Named arguments** (or keyword arguments) are passed by explicitly specifying the parameter name, allowing them to be provided in any order.

- Example: 

```python
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alice", "Hello")           # Positional
greet(greeting="Hi", name="Bob")  # Named
```

In this example, the `greet` function can be called with positional or named arguments. This provides flexibility in how the function is called.

---

