# Exception handling

## Q1. What is exception handling in Python?

`Answer1:` Exception handling is a mechanism in Python that allows developers to manage errors and exceptional conditions gracefully without crashing the program. It involves using try, except, else, and finally blocks to catch and handle exceptions.

## Q2. Explain the try and except blocks with an example?

`Answer2:` The try block contains code that might raise an exception, while the except block handles the exception if it occurs.

```bash
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")  # OUTPUT: Cannot divide by zero!
```

## Q3. What is the purpose of the finally block?

`Answer3:` The finally block contains code that will execute regardless of whether an exception was raised or not. It's typically used for cleanup actions like closing files or releasing resources.

## Q4. Can you have multiple except blocks for a single try? Explain?

`Answer4:` Yes, you can have multiple except blocks to handle different types of exceptions separately.

```bash
try:
    # code that may raise multiple exceptions
except ValueError:
    # handle ValueError
except TypeError:
    # handle TypeError
```

## Q5. What is the else block used for in exception handling?

`Answer5:` The else block executes only if no exceptions were raised in the try block. It's useful for code that should run only when the try block succeeds without errors.

## Q6. How do you catch multiple exceptions in a single except block?

`Answer6:` You can catch multiple exceptions by specifying a tuple of exception types in a single except block.

```bash
try:
    # code that may raise multiple exceptions
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")
```

## Q7. What is the difference between Exception and BaseException in Python?

`Answer7:` BaseException is the base class for all exceptions, including system-exiting exceptions like SystemExit, KeyboardInterrupt, and GeneratorExit. Exception is a subclass of BaseException and is the base class for most user-defined and built-in exceptions. It's recommended to inherit from Exception when creating custom exceptions.

## Q8. How can you retrieve the traceback information of an exception?

`Answer8:` You can retrieve traceback information using the traceback module or by accessing the exception's __traceback__ attribute.

```bash
import traceback

try:
    1 / 0
except ZeroDivisionError as e:
    traceback.print_exc()
```

## Q9. Explain the use of the raise statement in exception handling?

`Answer9:` The raise statement is used to manually trigger an exception. It can be used to re-raise an existing exception or to raise a new one.

```bash
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
```

## Q10. What is a custom exception, and how do you create one in Python?

`Answer 10:` A custom exception is a user-defined exception that allows developers to create specific error types for their applications. It is created by subclassing the Exception class.

```bash
class MyCustomError(Exception):
    """Custom exception for specific error conditions."""
    pass
```

## Q11. How does exception handling affect performance in Python?

`Answer 11:` Exception handling can introduce some overhead, especially if exceptions are raised frequently. However, for normal control flow where exceptions are rare, the performance impact is negligible. It's best to use exceptions for exceptional conditions, not for regular control flow.

## Q12. Explain exception chaining and the from keyword?

`Answer 12:` Exception chaining allows one exception to be raised while preserving the original exception context. The from keyword is used to explicitly chain exceptions.

```bash
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("Invalid operation") from e
```

## Q13. What are context managers, and how do they relate to exception handling?

`Answer 13:` Context managers manage resources like files or network connections, ensuring they are properly acquired and released. They use the with statement, which internally uses try-finally to handle exceptions and ensure resources are cleaned up.

```bash
with open('file.txt', 'r') as file:
    data = file.read()
```

## Q14. Describe how you would handle exceptions in a multithreaded Python application?

`Answer 14:` In multithreaded applications, each thread should handle its own exceptions. Unhandled exceptions in threads typically terminate the thread without affecting others. To manage exceptions, wrap thread execution code in try-except blocks and consider using thread-safe logging mechanisms to report errors.

## Q15. Can you explain the difference between sys.exc_info() and traceback module for exception handling?

`Answer 15:` sys.exc_info() returns a tuple containing information about the current exception being handled, including the exception type, value, and traceback. The traceback module provides utilities to extract, format, and print stack traces, allowing for more detailed and formatted exception information.

```bash
import sys, traceback

try:
    1 / 0
except ZeroDivisionError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback)
```

## Q16 List out the Exception Handling types

`Answer 16:`

- Try - Try block lets you test a block of code for error.
- Except - It block lets you handle the error
- Else - else block let you execute code when there is no error
- Finally - It block lets you execute code regardless of the result of the try and except block
- Raise - raise key word is used to raise an exception

## Q17 List out the types of error

`Answer 17:`

- `syntex Error` - Raised when the parser encounters a syntax error in the code.

```python
# Missing colon after if statement
if True
    print("Hello, World!")
```

`Output:`

```bash
File "example.py", line 2
    if True
           ^
SyntaxError: invalid syntax
```

- `Types Error` - Raised when an operation or function is applied to an object of inappropriate type.

```python
# Attempting to add a string and an integer
result = '2' + 2
```

`Output:`

```python
TypeError: can only concatenate str (not "int") to str
```

- `Name Error` - Raised when a local or global name is not found. It indicates that a variable or function name is not defined.

```python
# Using an undefined variable
print(undefined_variable)
```

`Output:`

```python
NameError: name 'undefined_variable' is not defined
```

- `Index Error` - Raised when a sequence subscript is out of range. It occurs when trying to access an index that doesn't exist in a list, tuple, or other indexable objects.

```python
# Accessing an index that is out of range
lst = [1, 2, 3]
print(lst[5])
```

`Output:`

```python
IndexError: list index out of range
```

- `Key Error` - Raised when a dictionary key is not found in the set of existing keys.

```python
# Accessing a non-existent key in a dictionary
d = {'a': 1}
print(d['b'])
```

`Output:`

```python
KeyError: 'b'
```

- `Value Error` - Raised when a function receives an argument of the correct type but an inappropriate value.

```python
# Converting a non-numeric string to integer
int('abc')
```

`Output:`

```python
ValueError: invalid literal for int() with base 10: 'abc'
```

- `Attribute Error` - Raised when an attribute reference or assignment fails. This occurs when trying to access or assign an attribute that doesn't exist for an object.

```python
# Converting a non-numeric string to integer
int('abc')
```

`Output:`

```python
ValueError: invalid literal for int() with base 10: 'abc'
```

- `IOError` - Raised when an I/O operation (such as reading or writing a file) fails for an I/O-related reason. In Python 3, many IOError exceptions have been merged into OSError.

```python
# Attempting to open a non-existent file for reading
with open('nonexistent_file.txt', 'r') as f:
    pass
```

`Output:`

```python
FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
```

- `Zerro Division Error` - Raised when the second argument of a division or modulo operation is zero.

```python
# Division by zero
result = 10 / 0
```

`Output:`

```python
ZeroDivisionError: division by zero
```

- `Import Error` - Raised when an imported module cannot be found or loaded.

```python
# Attempting to import a non-existent module
import nonexistent_module
```

`Output:`

```python
ModuleNotFoundError: No module named 'nonexistent_module'
```

## Programming Exercises

### Exercise 1: Handling Multiple Exceptions

`Problem:`

Write a function process_data(data) that takes a list of integers and returns the reciprocal of each number in a new list. The function should handle the following exceptions:

ValueError if the input is not a list.
TypeError if an element in the list is not an integer or float.
ZeroDivisionError if an element is zero.

`Solution:`

```python
def process_data(data):
    try:
        if not isinstance(data, list):
            raise ValueError("Input must be a list.")
        
        reciprocals = []
        for num in data:
            try:
                reciprocals.append(1 / num)
            except TypeError:
                print(f"TypeError: Element {num} is not a number.")
            except ZeroDivisionError:
                print("ZeroDivisionError: Cannot compute reciprocal of zero.")
        
        return reciprocals
    except ValueError as ve:
        print(f"ValueError: {ve}")

# Example Usage
print(process_data([2, 0, 'a', 4]))
```

`Output:`

```bash
ERROR!
ZeroDivisionError: Cannot compute reciprocal of zero.
TypeError: Element a is not a number.
[0.5, 0.25]
```

### Exercise 2: Creating Custom Exceptions

`Problem:`

Create a custom exception NegativeNumberError that is raised when a negative number is encountered in a list of numbers. Write a function validate_numbers(numbers) that iterates through the list and raises NegativeNumberError if any number is negative. Otherwise, it returns True.

`Solution:`

```python
class NegativeNumberError(Exception):
    """Exception raised for negative numbers."""
    def __init__(self, number, message="Negative number encountered"):
        self.number = number
        self.message = f"{message}: {number}"
        super().__init__(self.message)

def validate_numbers(numbers):
    try:
        for num in numbers:
            if num < 0:
                raise NegativeNumberError(num)
        return True
    except NegativeNumberError as nne:
        print(nne)
        return False

# Example Usage
validate_numbers([10, 5, -3, 7])
```

`Output:`

```bash
Negative number encountered: -3
False
```

### Exercise 3: Resource Management with finally

`Problem:`

Write a function read_first_line(filepath) that opens a file, reads the first line, and returns it. Ensure that the file is properly closed regardless of whether an exception occurs (e.g., file not found).

`Solution:`

```bash
def read_first_line(filepath):
    try:
        file = open(filepath, 'r')
        line = file.readline()
        return line.strip()
    except FileNotFoundError:
        print(f"FileNotFoundError: The file {filepath} does not exist.")
    finally:
        try:
            file.close()
            print("File closed.")
        except NameError:
            # file was never opened
            pass

# Example Usage
print(read_first_line('example.txt'))
```

`Outputs:`

If example.txt exists:

```bash
[First line of the file]
File closed.
```

If example.txt does not exist:

```bash
FileNotFoundError: The file example.txt does not exist.
```

### Exercise 4: Exception Logging

`Problem:`

Enhance the following function to log exceptions to a file named error.log instead of printing them.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
```

`Solution:`

```python
import logging

# Configure logging
logging.basicConfig(filename='error.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.ERROR)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero.", exc_info=True)
        return None

# Example Usage
result = divide(10, 0)
```

`Explanation:`

The logging module is configured to write error messages to error.log with a timestamp and error level. When a ZeroDivisionError occurs, the exception details are logged instead of being printed.

### Exercise 5: Nested Exception Handling

`Problem:`

Write a function process_file(filepath) that performs the following steps:

- Opens a file and reads its content.
- Parses the content as JSON.
- Returns a specific value from the JSON data.
- Handle exceptions at each step appropriately, using nested try-except blocks.

`Solution:`

```python
import json

def process_file(filepath, key):
    try:
        try:
            with open(filepath, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"FileNotFoundError: The file {filepath} does not exist.")
            return
        except IOError as e:
            print(f"IOError while reading the file: {e}")
            return

        try:
            data = json.loads(content)
        except json.JSONDecodeError as je:
            print(f"JSONDecodeError: Invalid JSON format. {je}")
            return

        try:
            value = data[key]
            return value
        except KeyError:
            print(f"KeyError: The key '{key}' was not found in the JSON data.")
            return

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example Usage
result = process_file('data.json', 'name')
if result:
    print(f"Name: {result}")
```

`Explanation:`

The function process_file handles exceptions at each critical step:

- File Operations: Catches FileNotFoundError and IOError.
- JSON Parsing: Catches json.JSONDecodeError.
- Data Retrieval: Catches KeyError if the specified key is missing.

`Expected Outputs:`

- `Successful Execution:`

```bash
Name: John Doe
```

- `File Not Found:`

```bash
FileNotFoundError: The file data.json does not exist.
```

- `Invalid JSON:`

```bash
JSONDecodeError: Invalid JSON format. Expecting ',' delimiter: line 1 column 15 (char 14)
```

- `Missing Key:`

```bash
KeyError: The key 'name' was not found in the JSON data.
```
