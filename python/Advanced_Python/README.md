# Advanced Python

## Table of Contents

- [1. Advanced OOP Concepts](#advanced-oop-concepts)

- [2.  Concurrency and Parallelism](#concurrency-and-parallelism)

- [3.  Working with Databases](#working-with-databases)

- [4.  Data Science and Machine Learning Libraries](#data-science-and-machine-learning-libraries)

- [5. Web Development Frameworks](#web-development-frameworks)

- [6. Handling Large Files and Data](#handling-large-files-and-data)

- [7. Advanced Modules](#advanced-modules)

## Advanced OOP Concepts

### 1. Explain the concept of metaclasses in Python and provide a practical use case?

A metaclass in Python is a class of a class, meaning that a metaclass defines how classes behave. Just as classes define the behavior of instances, a metaclass defines the behavior of classes themselves. The default metaclass in Python is `type`, but custom metaclasses can be created by inheriting from `type`.

Metaclasses allow you to intercept and modify class creation. When a class is created, Python looks for the `metaclass` keyword and uses it to build the class. You can use a metaclass to customize or add behavior to the class creation process.

```python
class InterfaceMeta(type):
    def __new__(cls, name, bases, dct):
        if 'required_method' not in dct:
            raise TypeError(f"Class {name} must define 'required_method'")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=InterfaceMeta):
    def required_method(self):
        print("This is required.")

# Uncommenting this would raise an error because the required method is missing
# class InvalidClass(metaclass=InterfaceMeta):
#     pass
```

### 2. Write a Python program that demonstrates the Method Resolution Order (MRO) using multiple inheritance, and explain how MRO is determined in Python?

Python uses the C3 Linearization Algorithm to determine the Method Resolution Order (MRO) when a class inherits from multiple classes. This ensures that Python handles the "diamond problem" (where the same method might be present in multiple parent classes) correctly by defining a consistent order of method lookup.

The MRO can be viewed using the `mro()` method or `__mro__` attribute. Let's create an example demonstrating MRO in multiple inheritance.

```python
class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")

class C(A):
    def method(self):
        print("Method in C")

class D(B, C):
    pass

# Create an instance of class D
d = D()
d.method()  # This will call B's method

# Print the MRO of class D
print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

## Concurrency and Parallelism

### 1. What is the difference between concurrency and parallelism?

- **Concurrency** refers to the ability of a system to manage multiple tasks simultaneously by switching between them. The tasks don't necessarily execute at the same time but make progress simultaneously. It’s about structure.

- **Parallelism** refers to the simultaneous execution of multiple tasks, usually achieved by using multiple CPU cores. This is actual simultaneous execution of tasks. It’s about execution.

### 2. What is the GIL (Global Interpreter Lock), and how does it affect multithreading in Python?

The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes simultaneously. This means that only one thread can execute Python code at any time, which limits the performance gains from multithreading, especially for CPU-bound tasks. However, I/O-bound tasks like network requests can still benefit from multithreading since the GIL is released during I/O operations.

### 3. When would you use `multiprocessing` over `multithreading` in Python?

You should use `multiprocessing` when dealing with CPU-bound tasks, such as computational-heavy tasks (e.g., matrix operations, scientific computing), because the multiprocessing module creates separate memory spaces and new Python interpreters for each process, allowing true parallelism by utilizing multiple CPU cores. Multithreading is more suited for I/O-bound tasks (e.g., network requests) where the GIL is less of an issue.

### 4.  What are coroutines, and how do they relate to asyncio?

Coroutines are special functions in Python defined with the `async def` keyword. They allow for asynchronous execution by suspending their execution at certain points using the `await` keyword. This means they can "pause" execution while waiting for something (like I/O) and resume later, making them useful for non-blocking I/O operations. In Python’s `asyncio` framework, coroutines are the building blocks for creating asynchronous tasks.

### 5. Explain the Global Interpreter Lock (GIL) in Python and how it affects multithreading

The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecode simultaneously. This ensures that only one thread runs in the interpreter at any given time.

The GIL exists primarily due to the memory management in CPython, particularly reference counting for garbage collection. While it simplifies memory management, it also means that Python's multithreading is not suitable for CPU-bound tasks. Even if multiple threads are created, only one will run Python code at a time, resulting in little to no performance gains for CPU-intensive operations. However, GIL doesn't affect I/O-bound tasks like file I/O or network requests since threads can be switched when waiting for I/O operations to complete.

In contrast, Python's multiprocessing module spawns separate processes, each with its own interpreter and GIL, allowing for true parallelism and better performance in CPU-bound tasks.

### 6. How does Python’s `asyncio` module avoid blocking I/O operations, and how does it achieve concurrency?

`asyncio` achieves concurrency by using an event loop that runs asynchronous tasks, which are `coroutines`. Instead of blocking on I/O (e.g., waiting for network or file operations), the event loop can pause a coroutine that is waiting for I/O and switch to another coroutine that is ready to execute.

This non-blocking behavior is achieved using the `await` keyword. When a coroutine encounters an `await`, it pauses execution, allowing other tasks in the event loop to proceed. Once the awaited I/O operation is complete, the event loop resumes the paused coroutine.

Unlike threading or multiprocessing, `asyncio` doesn’t provide true parallelism but instead makes optimal use of the CPU by not waiting idly for I/O-bound tasks. It’s best suited for programs with many I/O operations, such as web servers or network clients, where tasks spend most of their time waiting for external data.

### 7. What are some of the key trade-offs or overheads involved when using Python’s `multiprocessing` module?

The `multiprocessing` module provides true parallelism by spawning multiple processes, but this comes with some trade-offs:

- **Memory Overhead:** Each process in `multiprocessing` has its own memory space, meaning that data is copied between processes, leading to higher memory usage than multithreading, where threads share memory.

- **Inter-process Communication (IPC) Overhead:** Processes cannot share memory as easily as threads, so communication between processes (via pipes, queues, or shared memory) introduces overhead.

- **Process Startup Time:** Creating processes is slower compared to threads due to the need to duplicate the entire process state, including memory, variables, and the Python interpreter.

- **Synchronization Complexity:** While threading has the GIL to protect shared data (although limiting performance), multiprocessing requires explicit synchronization (locks, semaphores) to ensure data integrity when processes need to share data.

- **Platform Limitations:** On Windows, multiprocessing uses the spawn method by default, which has higher overhead compared to Unix-like systems where the fork method is used.

### 8. Write a Python program using `asyncio` to scrape data from multiple URLs concurrently. Use `aiohttp` for making asynchronous HTTP requests?

```python
import asyncio
import aiohttp

# List of URLs to scrape
urls = [
    'https://example.com',
    'https://example.org',
    'https://example.net'
]

async def fetch(url, session):
    async with session.get(url) as response:
        print(f"Fetching {url}")
        return await response.text()

async def scrape_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(url, session)) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Main event loop
async def main():
    html_pages = await scrape_all(urls)
    for idx, html in enumerate(html_pages):
        print(f"\nHTML content from {urls[idx]}:\n{html[:200]}...")  # Print first 200 chars

# Run the event loop
asyncio.run(main())
```

### 9. Write a Python program using multiprocessing to find all prime numbers in a given range?

```python
import multiprocessing

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find primes in a given range
def find_primes_in_range(start, end):
    return [n for n in range(start, end) if is_prime(n)]

# Function to divide work across multiple processes
def parallel_prime_finder(n, num_processes=4):
    pool = multiprocessing.Pool(processes=num_processes)
    
    # Split the range into chunks based on the number of processes
    chunk_size = n // num_processes
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes)]
    
    # Find primes in parallel
    results = pool.starmap(find_primes_in_range, ranges)
    pool.close()
    pool.join()
    
    # Flatten results
    primes = [prime for sublist in results for prime in sublist]
    return primes

if __name__ == "__main__":
    n = 100000  # Range up to 100,000
    num_processes = 4  # Number of processes to use
    
    primes = parallel_prime_finder(n, num_processes)
    print(f"Found {len(primes)} prime numbers.")
```

### 10. Can you explain the difference between `asyncio.gather()` and `asyncio.create_task()`?

- `asyncio.gather()` is used to run multiple awaitable objects (like coroutines) concurrently and return their results as soon as all of them are done. It's like a way to wait for several coroutines to complete and collect their results.

- `asyncio.create_task()` is used to schedule the execution of a coroutine in the background. It doesn’t wait for the task to finish. You can use `create_task()` to run a coroutine and continue running other code concurrently, then later `await` or check on the task's completion if needed.

### 11. How does multiprocessing.Pool help in process management? Can you give an example?

`multiprocessing.Pool` provides a convenient way to parallelize the execution of a function across multiple input values. It manages a pool of worker processes, distributing the input data to them and collecting the results. This is especially useful when you want to apply a function to a large dataset in parallel.

Here’s a simple example using `multiprocessing.Pool` to compute squares of numbers in parallel:

```python
from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as pool:
        results = pool.map(square, range(10))
    print(results)
```

## Working with Databases

### 1. Explain ACID properties in a database and how they ensure reliable transaction processing

ACID stands for Atomicity, Consistency, Isolation, and Durability, which are crucial properties that guarantee the reliability of database transactions:

- `Atomicity:` A transaction is treated as a single, indivisible unit. Either all operations within the transaction are completed successfully, or none of them are. If any part of the transaction fails, the entire transaction is rolled back.
- `Consistency:` A transaction must move the database from one valid state to another. If any constraints (like foreign keys or checks) exist in the database schema, they must be maintained after the transaction.
- `Isolation:` Transactions should be executed independently of one another. Intermediate results of a transaction are not visible to other transactions until the transaction is completed.
- `Durability:` Once a transaction is committed, its effects are permanent, even in the event of a system failure (e.g., power outage or crash). This is ensured through mechanisms like transaction logs.

### 2. What is the difference between pessimistic and optimistic locking in databases?

- `Pessimistic Locking:` In pessimistic locking, a database system assumes that conflicts (e.g., data modifications) between concurrent transactions are likely to happen. Thus, it locks the resource (such as a row or table) early, ensuring no other transaction can modify it until the lock is released. This can lead to performance issues due to frequent locking.

  - `Use Case:` Ideal when conflicts are expected to be frequent, such as in high-contention environments.

- `Optimistic Locking:` In optimistic locking, the database assumes that conflicts are unlikely. Transactions are allowed to read and modify data without acquiring locks initially. Before committing the changes, the system checks whether another transaction has modified the data. If a conflict is detected, the transaction is rolled back and can be retried.

  - `Use Case:` Suitable when conflicts are rare, such as in low-contention environments where most transactions are read-heavy.

### 3. What are database indexes? How do they improve query performance, and what are the trade-offs?

A database index is a data structure that improves the speed of data retrieval operations on a table by allowing faster searching. It works similarly to an index in a book, helping the database engine locate specific rows more quickly, without scanning the entire table.

Indexes improve performance for read-heavy operations (e.g., `SELECT` queries), especially on large tables, but they come with trade-offs:

- `Storage Overhead:` Indexes require additional storage space, as a copy of some data is stored in the index.

- `Insert/Update/Delete Performance:` Maintaining indexes slows down `INSERT`, `UPDATE`, and `DELETE` operations, as the index must be updated whenever the underlying table data changes.

### 4. How does sharding work in distributed databases?

Sharding is a technique used in distributed databases to scale horizontally by dividing a large dataset across multiple database instances. Each shard is responsible for storing a portion of the dataset. This division can be done based on different criteria, such as ranges of a specific column (e.g., user IDs) or hashing a particular value.

**Benefits of sharding:**

- `Increased Performance:` By distributing data across multiple servers, you can process queries in parallel, reducing latency.

- `Scalability:` Sharding allows the system to scale horizontally as more data or traffic is added.

**Challenges:**

- `Complexity:` Implementing sharding introduces complexity in terms of managing cross-shard queries, maintaining consistency, and handling failovers.

- `Data Distribution:` Poorly chosen sharding keys can lead to data skew, where some shards store significantly more data than others, leading to performance bottlenecks.

### 5.  Write a Python function to fetch the 10 highest-paid employees from a table `employees` with columns `id`, `name`, and `salary`. The function should use SQLAlchemy to interact with an SQLite database?

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database model
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Integer)

# Create an SQLite engine and session
engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Function to get top 10 highest-paid employees
def get_top_paid_employees():
    # Query top 10 employees based on salary
    top_employees = session.query(Employee).order_by(Employee.salary.desc()).limit(10).all()

    # Print the result
    for emp in top_employees:
        print(f"ID: {emp.id}, Name: {emp.name}, Salary: {emp.salary}")

# Call the function to get top 10 employees
get_top_paid_employees()

# Close the session
session.close()
```

### 6. Write a Python program using sqlite3 to create a table products, insert three records, and fetch all products whose price is greater than 100?

```python
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the 'products' table
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL
                )''')

# Insert some product records
products = [
    ('Laptop', 999.99),
    ('Mouse', 49.99),
    ('Keyboard', 149.99)
]
cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', products)

# Commit the changes
conn.commit()

# Query products with price > 100
cursor.execute('SELECT * FROM products WHERE price > 100')
rows = cursor.fetchall()

# Print the products
for row in rows:
    print(row)

# Close the connection
conn.close()
```

## Data Science and Machine Learning Libraries

### 1. What is NumPy, and why is it important in data science?

NumPy (Numerical Python) is a fundamental library for numerical computing in Python. It provides support for multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays. NumPy is crucial because it offers efficient array operations, which form the foundation of many data science tools and libraries like Pandas, Scikit-learn, and more.

### 2. What is the difference between a Pandas Series and a DataFrame?

A Series is a one-dimensional labeled array capable of holding any data type (like an array with labels). A DataFrame is a two-dimensional labeled data structure, similar to a table or a spreadsheet, where each column is a Series.

### 3. Explain what machine learning is in simple terms?

Machine learning is a branch of artificial intelligence that allows computers to learn from data without being explicitly programmed. The machine finds patterns in the data and uses them to make decisions or predictions.

### 4. What is the difference between Supervised and Unsupervised Learning?

In supervised learning, the model is trained using labeled data (i.e., input data paired with the correct output). In unsupervised learning, the model works with unlabeled data and tries to find patterns or groupings (e.g., clustering).

### 5. Explain the bias-variance tradeoff

The bias-variance tradeoff refers to balancing the error introduced by the bias (error due to overly simplistic models) and variance (error due to overly complex models). A model with high bias oversimplifies the data and underfits, while a model with high variance overfits the training data but performs poorly on unseen data.

### 6. What is the purpose of cross-validation in machine learning?

Cross-validation is a technique used to assess how well a model generalizes to unseen data. It splits the dataset into multiple parts (folds), trains the model on some folds, and tests it on the remaining fold. This process is repeated to ensure that the model's performance is robust and not biased by a particular split.

### 7. What is regularization in machine learning, and why is it useful?

Regularization is a technique used to prevent overfitting by adding a penalty to the loss function. It discourages the model from learning overly complex patterns that work well on training data but do not generalize to unseen data. Common forms of regularization include L1 (Lasso) and L2 (Ridge), which add a penalty on the magnitude of model coefficients.

### 8. What are precision and recall? How are they used to evaluate a classification model?

Precision is the ratio of true positive predictions to the total predicted positives. It measures how many selected items are relevant. Recall is the ratio of true positives to all actual positives (including the false negatives). Precision and recall are particularly important when dealing with imbalanced datasets where one class dominates.

### 9. Explain the difference between Bagging and Boosting

Bagging (e.g., Random Forest) is an ensemble technique where multiple weak models (typically decision trees) are trained independently in parallel on random subsets of the data. The final prediction is the average or majority vote of all models. Boosting (e.g., Gradient Boosting) trains models sequentially, where each new model focuses on the errors of the previous models, thus improving performance iteratively.

### 10. Create a NumPy array of integers from 0 to 9 and replace all even numbers with -1.      (NumPy Array Operations)

```python
import numpy as np

arr = np.arange(10)
arr[arr % 2 == 0] = -1
print(arr)
```

### 11. Create a DataFrame with two columns, Name and Score. Filter the rows where Score is greater than 50. (Pandas DataFrame Manipulation)

```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [45, 85, 60]}
df = pd.DataFrame(data)

filtered_df = df[df['Score'] > 50]
print(filtered_df)
```

### 12. Using Pandas and Scikit-learn, load a dataset, split it into training and testing sets, train a linear regression model, and print the model’s coefficients. (Train-Test Split & Linear Regression)

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Example dataset
data = {'Area': [2600, 3000, 3200, 3600, 4000], 'Price': [550000, 565000, 610000, 680000, 725000]}
df = pd.DataFrame(data)

# Features and target
X = df[['Area']]
y = df['Price']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Output coefficients
print(f'Coefficients: {model.coef_}')
```

### 13. Use the tips dataset from Seaborn to create a scatterplot showing the relationship between `total_bill` and `tip`. (Data Visualization with Seaborn)

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')

# Create a scatterplot
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()
```

### 14. Use Scikit-learn to perform Grid Search for hyperparameter tuning on a Random Forest Classifier. Optimize for `n_estimators` and `max_depth`. (Grid Search for Hyperparameter Tuning)

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Initialize the model
rf = RandomForestClassifier(random_state=42)

# Define hyperparameters grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7]
}

# Perform grid search
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)
grid_search.fit(X, y)

# Output the best parameters
print(f'Best Parameters: {grid_search.best_params_}')
```

### 15. Perform PCA on the Iris dataset to reduce its dimensionality to 2 components. Plot the result. (Principal Component Analysis (PCA))

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Perform PCA to reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot the PCA results
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('PCA on Iris Dataset')
plt.show()
```

## Web Development Frameworks

### 1. What is a Python Web Framework?

A Python web framework is a software framework designed to aid in the development of web applications, including web services, APIs, and web resources. It provides a structured way to build and deploy web applications by providing tools and libraries for common tasks such as URL routing, database interaction, and handling requests and responses.

### 2. How many frameworks are there in Python?

There are numerous Python web frameworks available, with the most popular ones being Django, Flask, FastAPI, Pyramid, and Tornado. The exact number varies as new frameworks are developed and others may become obsolete, but there are dozens of options catering to different needs and preferences.

### 3. Why Python frameworks are needed?

Python frameworks are needed to streamline the web development process. They provide built-in tools and libraries that handle routine tasks, reduce redundancy, improve code organization, and enhance productivity. Frameworks also help maintain best practices and security standards, making it easier to build reliable and scalable applications.

### 4. Is PyCharm a framework in Python?

No, PyCharm is not a framework; it is an integrated development environment (IDE) used for programming in Python. It provides tools for coding, debugging, and testing but does not offer the specific functionalities of a web framework.

### 5. What are the benefits of using Python frameworks?

The benefits of using Python frameworks include:

- **Efficiency:** They speed up the development process by providing reusable components and pre-built functionalities.

- **Scalability:** Frameworks often include features that help applications scale effectively.

- **Security:** They provide built-in security features, reducing the likelihood of common vulnerabilities.

- **Community Support:** Popular frameworks have large communities that offer documentation, tutorials, and third-party plugins.

- **Maintainability:** They encourage clean code practices and project organization, making it easier to maintain and update applications.

### 6. What is Django in Python?

Django is a high-level web framework for Python that simplifies the process of building web applications. It follows the model-template-view (MTV) architectural pattern, promoting rapid development and clean, pragmatic design. Django provides a set of tools and libraries that facilitate the creation of web applications with built-in features such as authentication, URL routing, and database management.

### 7. Is Python Django frontend or backend?

Django is primarily a backend web framework. It is used to handle server-side logic, database interactions, and application functionality. While Django can serve HTML templates for the frontend, it does not directly manage frontend technologies like HTML, CSS, or JavaScript, which are usually handled by other frameworks or libraries.

### 8. What is Django used for in Python?

Django is used for building web applications, including:

- Content management systems (CMS)

- E-commerce sites

- Social networking sites

- Data-driven websites

- APIs for mobile and web applications It provides features like an ORM (Object-Relational Mapping) for database interactions, an admin interface, and tools for user authentication and security.

### 9. How does Django work with Python?

Django works with Python by utilizing its syntax and features to create web applications. Developers write Django applications in Python, defining models (data structures), views (business logic), and templates (presentation logic) in Python code. Django handles HTTP requests, interacts with the database, and returns HTML responses using Python’s built-in features and libraries.

### 10. How is Django different from Python?

Django and Python are not directly comparable since Django is a framework built using the Python programming language. Here are some key differences:

- **Nature:** Python is a programming language, while Django is a web framework that uses Python.
- **Purpose:** Python is a general-purpose language used for various applications (web development, data science, scripting, etc.), while Django is specifically designed for building web applications.

- **Features:** Django provides additional tools and libraries to streamline web development that Python alone does not offer.

### 11. What is Python Flask good for?

Flask is a lightweight web framework for Python, ideal for building small to medium-sized web applications and APIs. It’s particularly well-suited for projects that require flexibility and simplicity. Flask is good for:

- Prototyping and building minimum viable products (MVPs).

- Creating RESTful APIs.

- Developing microservices.

- Building single-page applications (SPAs) when combined with frontend frameworks.

### 12. What are the features of Python Flask?

Some notable features of Flask include:

- **Lightweight and Flexible:** Flask is minimalistic, allowing developers to choose components based on their project needs.

- **Built-in Development Server:** It includes a lightweight server for testing and debugging during development.

- **Jinja2 Templating:** Flask uses Jinja2 for rendering templates, allowing developers to create dynamic web pages.

- **RESTful Request Dispatching:** It supports RESTful request handling for building APIs.

- **Extensible:** Flask can be easily extended with various plugins and libraries.

- **Integrated Unit Testing Support:** It includes tools for testing applications.

- **Support for Cookies and Sessions:** Flask provides mechanisms to manage user sessions and cookies.

### 13. Is Python Flask frontend or backend?

Flask is primarily a backend web framework. It handles server-side logic, database interactions, and application functionality. While it can serve HTML templates for the frontend, the actual frontend technologies (HTML, CSS, JavaScript) are usually handled separately.

### 14. How does Flask work in Python?

Flask works in Python by allowing developers to define routes (URLs), request handlers (functions that respond to requests), and templates (HTML with dynamic content). When a user makes a request to a Flask application, the framework matches the request to the corresponding route and executes the associated view function. Flask manages the request and response cycle, enabling the application to respond with the appropriate content.

### 15. Which is better: Flask or Django in Python? Explain with reason?

The choice between Flask and Django depends on the specific needs of the project:

- Flask is better for:

  - **Simplicity and Flexibility:** If you want a lightweight framework for small projects or microservices.

  - **Customization:** Flask allows for greater customization, making it easier to pick and choose components.

  - **Prototyping:** It’s often quicker to set up for MVPs or proof-of-concept applications.

- Django is better for:

  - **Feature-Rich Applications:** If you need a lot of built-in functionality (e.g., authentication, ORM, admin panel).

  - **Scalability:** Django is designed for larger applications and can handle more complex needs out of the box.
  
  - **Rapid Development:** It has a comprehensive ecosystem that can speed up development for more extensive applications.

### 16. What is Building REST APIs?

REST (Representational State Transfer) is an architectural style for designing networked applications, where clients and servers communicate via standard HTTP methods such as GET, POST, PUT, DELETE, etc.

## Handling Large Files and Data

### 1. What is the difference between CSV and JSON formats?

CSV (Comma-Separated Values) is a simple text format that uses commas to separate values, typically used for tabular data. It does not support nested structures and is less flexible in terms of data representation. JSON (JavaScript Object Notation), on the other hand, is a lightweight data interchange format that supports nested structures, arrays, and various data types, making it more versatile for representing complex data.

### 2. How can you handle large JSON files in Python without loading the entire file into memory?

To handle large JSON files efficiently, you can read and process the file line by line or in chunks using libraries like json or pandas. Using json with a line-by-line approach is memory-efficient since you process one record at a time, avoiding the need to load the entire file into memory.

### 3. What are some strategies for processing large XML files efficiently in Python?

Strategies for processing large XML files efficiently include:

- **Streaming Parsing:** Using libraries like `lxml` or `xml.etree.ElementTree` that support iterative parsing (e.g., `iterparse`) to handle large files without loading the entire file into memory.

- **Selective Element Processing:** Processing only specific elements that meet certain criteria to minimize memory usage.

- **Memory Management:** Clearing processed elements from memory to prevent memory overflow.

### 4. Write a Python function to read a CSV file and print the first 5 rows?

```python
import pandas as pd

def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    print(df.head())

# Example usage:
# read_csv_file('example.csv')
```

### 5. Write a Python function that processes a large JSON file containing multiple records, filtering out records based on a specific condition and saving the results to a new JSON file?

```python
import json

def filter_json(input_file, output_file, threshold):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            record = json.loads(line)
            if record['value'] > threshold:
                json.dump(record, outfile)
                outfile.write('\n')

# Example usage:
# filter_json('large_file.json', 'filtered_file.json', 100)
```

### 6. Write a Python script using lxml to parse a large XML file, filtering and printing elements based on a specific condition?

```python
from lxml import etree

def parse_large_xml(file_path, threshold):
    context = etree.iterparse(file_path, events=('end',), tag='YourTagName')
    for event, elem in context:
        if int(elem.find('YourChildTagName').text) > threshold:
            print(etree.tostring(elem, pretty_print=True).decode())
        elem.clear()  # Clear the element to save memory

# Example usage:
# parse_large_xml('large_file.xml', 100)
```

## Advanced Modules

### 1. What is the purpose of the logging module in Python?

The logging module in Python is used for tracking events that happen during the execution of a program. It provides a way to log messages with varying levels of severity (DEBUG, INFO, WARNING, ERROR, CRITICAL), allowing developers to monitor application behavior and troubleshoot issues.

### 2. What is a context manager in Python, and how can the contextlib module enhance its functionality?

A context manager in Python is an object that defines the runtime context to be established when executing a with statement. It is used to manage resources such as files, database connections, etc. The contextlib module provides utilities to create and work with context managers, allowing for cleaner and more manageable code.

### 3. Explain how threading works in Python and the role of the queue module in managing tasks among threads

Threading in Python allows for concurrent execution of code, enabling multiple threads to run in the same process. This can help with I/O-bound tasks, improving application responsiveness. The queue module provides a thread-safe way to manage tasks between producer and consumer threads, allowing for safe communication and data exchange without the need for explicit locking.

### 4. How is Logging used in Python?

Logging in Python is used by importing the logging module and configuring it to record messages to different outputs, such as the console, files, or external systems. It can be customized to log messages at various levels of severity

```python
import logging
logging.basicConfig(level=logging.DEBUG)  # Configures the lowest level of messages to display
logging.info("This is an info message")
logging.error("This is an error message")
```

### 5. How do you create a logging level in Python?

In Python, logging levels are predefined, but you can define your own by calling `logging.addLevelName(level, levelName)`

```python
import logging
MY_LOG_LEVEL = 25
logging.addLevelName(MY_LOG_LEVEL, "MY_LOG_LEVEL")
logging.log(MY_LOG_LEVEL, "This is a custom log level message.")
```

- **DEBUG**- Information for problem diagnostics only.
- **INFO**- The program runs as expected.
- **WARNING**- To indicate that something went wrong.
- **ERROR**- This means the software no longer functions.
- **CRITICAL**- For a very serious error.

### 6. Write a simple Python program that logs an error message when a division by zero occurs?

```python
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
        return None

# Test the function
result = divide(10, 0)
print(result)  # Output: None
```

### 7. Create a custom context manager using the contextlib module that manages a file resource. The context manager should write a message to the file and ensure the file is properly closed afterward

```python
from contextlib import contextmanager

@contextmanager
def managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

# Usage of the context manager
with managed_file('test.txt') as f:
    f.write('Hello, World!')

# Check the contents of the file
with open('test.txt', 'r') as f:
    print(f.read())  # Output: Hello, World!
```

### 8. Write a program that creates multiple threads to process items from a queue. The main thread should add items to the queue, while worker threads should process these items

```python
import threading
import queue
import time

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f'Processing {item}')
        time.sleep(1)  # Simulating work
        q.task_done()

# Create a queue
q = queue.Queue()
threads = []

# Create worker threads
for i in range(3):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
    threads.append(t)

# Add items to the queue
for item in range(10):
    q.put(item)

# Block until all tasks are done
q.join()

# Stop workers
for _ in threads:
    q.put(None)
for t in threads:
    t.join()
```
