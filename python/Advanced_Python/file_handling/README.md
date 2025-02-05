# File Handling Interview Questions

**1. What is file handling in Python?**

**Ans:**  File handling in Python refers to the ability to create, read, update, and delete files. Python provides several built-in functions and methods for file operations, such as `open()`, `read()`, `write()`, and `close()`. It supports different modes like read mode (`'r'`), write mode (`'w'`), append mode (`'a'`), and others for handling files.

**2. How do you open a file in Python?**

**Ans:**  In Python, the `open()` function is used to open a file. It takes two main arguments: the file name and the mode (optional).

Example:

```python
file = open('example.txt', 'r')  # Opens the file in read mode
```

**3. What are the different file modes in Python?**

**Ans:**  The file modes in Python are:

- `'r'`: Read mode (default). Opens the file for reading; raises an error if the file does not exist.
- `'w'`: Write mode. Opens the file for writing and truncates the file if it exists, or creates a new file.
- `'a'`: Append mode. Opens the file for writing and appends data to the end if the file exists, or creates a new file.
- `'x'`: Exclusive creation mode. Creates a new file but raises an error if the file already exists.
- `'b'`: Binary mode. Used for binary files (e.g., images, videos).
- `'t'`: Text mode (default). Used for text files.
  
**4. How do you read a file in Python?**

**Ans:**  Python provides multiple ways to read a file:

- `read()`: Reads the entire file.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all lines and returns them as a list.

Example:

```python
file = open('example.txt', 'r')
content = file.read()  # Reads the entire file
print(content)
file.close()
```

**5. How can you write to a file in Python?**

**Ans:**  You can write to a file using the `write()` or `writelines()` methods. The file must be opened in `'w'` (write) or `'a'` (append) mode.

Example:

```python
file = open('example.txt', 'w')
file.write('Hello, world!')  # Overwrites the file with 'Hello, world!'
file.close()
```

**6. What is the difference between `w` and `a` modes in file handling?**

**Ans:**

- `w` (write mode): Opens a file for writing and truncates it (i.e., deletes the file contents if it exists) before writing new data.
- `a` (append mode): Opens a file for writing and appends data at the end without deleting the existing content.

**7. What is the significance of using the `with` statement in file handling?**

**Ans:**  The `with` statement simplifies file handling by automatically closing the file after the block of code is executed. It ensures that the file is properly closed, even if an exception occurs.

Example:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# No need to explicitly close the file
```

**8. How do you check if a file exists before performing file operations?**

**Ans:**  To check if a file exists, you can use the `os.path.exists()` method from the `os` module or the `Path` object from the `pathlib` module.

Example using `os`:

```python
import os
if os.path.exists('example.txt'):
    print('File exists')
else:
    print('File does not exist')
```

Example using `pathlib`:

```python
from pathlib import Path
if Path('example.txt').exists():
    print('File exists')
else:
    print('File does not exist')
```

**9. What happens if you try to read a file that doesn’t exist?**

**Ans:**  If you attempt to read a non-existent file using the `open()` function with `'r'` mode, Python raises a `FileNotFoundError`.

Example:

```python
try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print('File not found!')
```

**10. What is the difference between binary mode and text mode in file handling?**

**Ans:**

- Text mode (`'t'`): Used for handling text files. The data is automatically encoded/decoded between strings and bytes.
- Binary mode (`'b'`): Used for handling binary files (e.g., images, videos). The data is read or written as raw bytes without encoding or decoding.

Example of opening a file in binary mode:

```python
file = open('image.png', 'rb')  # Opens a binary file in read mode
```

**11. How can you delete a file in Python?**

**Ans:**  You can delete a file using the `remove()` function from the `os` module.

Example:

```python
import os
os.remove('example.txt')  # Deletes the file named 'example.txt'
```

**12. How do you handle file exceptions in Python?**

**Ans:**  You can use `try-except` blocks to handle exceptions related to file operations, such as `FileNotFoundError`, `PermissionError`, etc.

Example:

```python
try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print('File not found!')
except PermissionError:
    print('You do not have permission to access this file.')
finally:
    print('Attempted file operation.')
```

**13. How do you read and write CSV files in Python?**

**Ans:**  Python provides the `csv` module to read from and write to CSV files.

You can use the csv module to read and write CSV files in Python. It provides functions like csv.reader() and csv.writer().

Example of reading a CSV file:

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

Example of writing to a CSV file:

```python
import csv

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])
```

**14. What is the difference between the readlines() and readline() methods when reading a file?**

**Ans:** readlines() reads all lines in the file into a list, while readline() reads one line at a time

**15. What is the purpose of the os.rename() function in file handling?**

**Ans:** The os.rename() function is used to rename files or directories in Python.

**16. Explain the difference between absolute and relative file paths.**

**Ans:**  An absolute file path specifies the file’s location starting from the root directory (or the drive on Windows). It gives the full path to the file, regardless of where the program is being executed. A relative file path specifies the file’s location relative to the current working directory, allowing the program to access files without specifying the entire path.

- **Absolute Path Example:**

  - On Windows: `C:\Users\Username\Documents\example.txt`
  - On Linux/Mac: `/home/username/Documents/example.txt`

- **Relative Path Example:**  
    If the current working directory is `/home/username/`, a relative path to the same file would be:

  - `Documents/example.txt`

**17. How can you read and write binary files in Python?**

**Ans:** You can read and write binary files in Python by using the ‘rb’ (read binary) and ‘wb’ (write binary) modes, respectively.

**18. How do you check if a file is a directory or a regular file in Python?**

**Ans:** You can use the os.path.isdir() and os.path.isfile() functions to check if a path corresponds to a directory or a regular file.

**18. How can you read and write JSON files in Python?**

****Ans:****  Python provides the `json` module to read from and write to JSON files. JSON (JavaScript Object Notation) is a popular format for exchanging data between servers and clients.

**Reading JSON Files:**

You can use the `json.load()` method to read a JSON file and convert it into a Python dictionary.

Example:

```python
import json

# Reading a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)  # The JSON content is now a Python dictionary
```

**Writing to JSON Files:**

You can use the `json.dump()` method to write Python data (such as a dictionary or list) to a JSON file.

Example:

```python
import json

# Python dictionary to write to a JSON file
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Writing to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # `indent` formats the JSON with 4 spaces for readability
```

**19. How do you move a file in Python from one directory to another?**

**Ans:**  To move a file from one directory to another in Python, you can use the `shutil.move()` method from the `shutil` module. This method moves the file to the target location, and if a file with the same name already exists in the target directory, it will overwrite the existing file.

Example:

```python
import shutil

# Source path of the file you want to move
source = 'path/to/source/file.txt'

# Destination path where you want to move the file
destination = 'path/to/destination/file.txt'

# Move the file
shutil.move(source, destination)

print("File moved successfully!")
```

- **`source`**: The current path of the file you want to move.
- **`destination`**: The target path where the file should be moved.

**20. Explain the purpose of the os.getcwd() function in file handling.**

**Ans:** os.getcwd() returns the current working directory, which is the directory where Python is currently executing.

**21. What is the purpose of the os.path.isabs() function in file handling?**

**Ans:** os.path.isabs() checks if a path is an absolute path (starts from the root directory).

**22. How do you read and write binary files using the `pickle` module in Python?**

**Ans:**  The `pickle` module in Python is used to serialize and deserialize Python objects, meaning it converts Python objects into a binary format (called "pickling") that can be saved to a file and later loaded back (called "unpickling"). This is useful for saving complex objects like dictionaries, lists, or custom class instances to files.

**Writing (Pickling) Binary Files:**
To write a Python object to a binary file using `pickle`, you use the `pickle.dump()` method.

Example:

```python
import pickle

# Python object to pickle (save)
data = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Open a binary file in write mode
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)  # Pickle (serialize) the data and write it to the file

print("Data has been pickled and written to data.pkl")
```

- `wb`: Stands for "write binary" mode.
- `pickle.dump(data, file)`: Serializes (`pickles`) the `data` and writes it to the `file`.

---

**Reading (Unpickling) Binary Files:**
To read a pickled object from a binary file, you use the `pickle.load()` method.

Example:

```python
import pickle

# Open the binary file in read mode
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)  # Unpickle (deserialize) the data

print("Unpickled data:", loaded_data)
```

- `rb`: Stands for "read binary" mode.
- `pickle.load(file)`: Reads the pickled binary data from the file and converts it back into the original Python object.

**23. What is the purpose of the os.path.basename() function in file handling?**

**Ans:** os.path.basename() extracts the base name (filename) from a path, ignoring the directory part.

**24. What is the purpose of the os.makedirs() function in file handling?**

**Ans:** os.makedirs() is used to create multiple directories in a specified path, including any necessary parent directories.

**25. Explain the purpose of the os.getcwd() function in file handling.**

**Ans:** os.getcwd() returns the current working directory, which is the directory where Python is currently executing.
