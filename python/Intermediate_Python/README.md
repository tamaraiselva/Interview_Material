# Intermediate Python

## Table of Contents

- [1. Object-Oriented Programming (OOP)](#Object-Oriented-Programming-(OOP))

- [2.  Modules and Packages](#Modules-and-Packages)

- [3.  Working with Files](#Working-with-Files)

- [4.  Decorators and Generators](#Decorators-and-Generators)

- [5. Comprehensions](#Comprehensions)

- [6. Regular Expressions (Regex)](#Regular-Expressions-(Regex))

- [7. Lambda Functions and Functional Programming](#Lambda-Functions-and-Functional-Programming)

- [8. Error Handling (Advanced)](#Error-Handling-(Advanced))

- [9. Unit Testing](#Unit-Testing)

## Object-Oriented Programming (OOP)

### 1. What is Object Oriented Programming (OOP)?

`Answer:`

Object-Oriented Programming (OOP) is a programming paradigm centered around the concept of "objects," which are instances of classes. OOP organizes software design around data, or objects, rather than functions and logic. The primary goal is to increase modularity, reusability, and scalability by bundling related properties and behaviors into individual objects.

`Key Features:`

- `Classes and Objects:` Blueprints and instances.
- `Encapsulation:` Hiding internal states.
- `Inheritance:` Reusing code through hierarchical relationships.
- `Polymorphism:` Ability to process objects differently based on their data type or class.
- `Abstraction:` Simplifying complex reality by modeling classes appropriate to the problem.

`Program Example:`

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

# Creating an object (instance) of Car
my_car = Car("Toyota", "Corolla")
my_car.display_info()  # Output: Toyota Corolla
```

### 2. Explain the Four Pillars of OOP

The four pillars of OOP are fundamental concepts that provide a foundation for designing and implementing object-oriented software.

- `a. Encapsulation`

`Definition:` Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class. It restricts direct access to some of an object's components, which is a means of preventing unintended interference and misuse.

`Implementation in Python:`

```python
class Person:
    def __init__(self, name, age):
        self.__name = name    # Private attribute
        self._age = age       # Protected attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Invalid age.")

# Usage
person = Person("Alice", 25)
print(person.get_name())  # Output: Alice
person.set_age(26)
print(person.get_age())   # Output: 26
# Direct access is restricted
# print(person.__name)    # AttributeError
```

- `b. Inheritance`

`Definition:` Inheritance allows a new class (child or subclass) to acquire the properties and behaviors of an existing class (parent or superclass). It promotes code reusability and establishes a relationship between classes.

`Example:`

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Inheriting from Employee
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Initialize parent class attributes
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")

# Usage
manager = Manager("John Doe", 80000, "Sales")
manager.display_details()

# Output:
# Name: John Doe, Salary: 80000
# Department: Sales
```

- `c. Polymorphism`

`Definition:` Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables methods to perform differently based on the object invoking them, even if they share the same name.

`Example:`

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def animal_sound(animal):
    animal.make_sound()

# Usage
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
```

- `d. Abstraction`

`Definition:` Abstraction involves hiding the complex implementation details of a system and exposing only the necessary parts. It allows programmers to focus on what an object does instead of how it does it.

`Implementation in Python:`

Using Abstract Base Classes (ABC) to define interfaces.

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Usage
def make_payment(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

credit = CreditCardProcessor()
paypal = PayPalProcessor()

make_payment(credit, 100)   # Output: Processing credit card payment of $100
make_payment(paypal, 200)   # Output: Processing PayPal payment of $200
```

### 3. What are Classes and Objects?

`Answer:`

`Classes:` A class is a blueprint for creating objects. It defines a set of attributes (data) and methods (functions) that the objects created from the class will have. Classes encapsulate data for the object and define behaviors associated with that data.

`Objects:` An object is an instance of a class. It represents a specific entity with its own unique state and behavior as defined by its class.

`Program Example:`

```python
class Student:
    # Class attribute
    school = "XYZ High School"

    def __init__(self, name, grade):
        self.name = name      # Instance attribute
        self.grade = grade    # Instance attribute

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, School: {Student.school}")

# Creating objects
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

# Using object methods
student1.display_info()  # Output: Name: Alice, Grade: A, School: XYZ High School
student2.display_info()  # Output: Name: Bob, Grade: B, School: XYZ High School
```

### 4. What is Inheritance? Provide an Example?

`Answer:`

Inheritance is a mechanism in OOP that allows a new class (child or subclass) to inherit attributes and methods from an existing class (parent or superclass). This promotes code reusability and establishes a hierarchical relationship between classes.

`Types of Inheritance:`

- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance

`Program Example:`

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Inheriting from Employee
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Initialize parent class attributes
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")

# Usage
manager = Manager("John Doe", 80000, "Sales")
manager.display_details()
# Output:
# Name: John Doe, Salary: 80000
# Department: Sales
```

### 5. What is Encapsulation and How is it Implemented in Python?

`Answer:`

Encapsulation is the OOP principle that binds together the data and the functions that manipulate the data, while keeping both safe from outside interference and misuse. It restricts direct access to some of an object's components, which can prevent the accidental modification of data.

`Implementation in Python:`

- `Private Attributes:` Prefixing attribute names with double underscores (__) makes them private.
- `Protected Attributes:` Prefixing attribute names with a single underscore (_) indicates they are protected (by convention).
- `Public Methods:` Providing getter and setter methods to access and modify private attributes.

`Program Example:`

```python
class Person:
    def __init__(self, name, age):
        self.__name = name    # Private attribute
        self._age = age       # Protected attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Invalid age.")

# Usage
person = Person("Alice", 25)
print(person.get_name())  # Output: Alice
person.set_age(26)
print(person.get_age())   # Output: 26
# Direct access is restricted
# print(person.__name)    # AttributeError
```

### 6. Explain Polymorphism with an Example?

`Answer:`

Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables the same operation to behave differently on different classes. This is typically achieved through method overriding, where a subclass provides a specific implementation of a method that is already defined in its superclass.

`Program Example:`

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def animal_sound(animal):
    animal.make_sound()

# Usage
dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
```

### 7. What is Abstraction? How is it Achieved in Python?

`Answer:`

Abstraction is the OOP principle of hiding complex implementation details and exposing only the necessary features of an object. It allows programmers to focus on what an object does rather than how it does it.

`Achieved in Python Using:`

- `Abstract Base Classes (ABC):` Using the abc module to create abstract classes and methods.
- `Interfaces:` Defining methods that must be implemented by subclasses.

`Program Example:`

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Usage
def make_payment(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

credit = CreditCardProcessor()
paypal = PayPalProcessor()

make_payment(credit, 100)   # Output: Processing credit card payment of $100
make_payment(paypal, 200)   # Output: Processing PayPal payment of $200
```

### 8. What are Dunder (Magic) Methods? Give Examples?

`Answer:`

Dunder methods, short for "double underscore" methods, are special methods in Python that begin and end with double underscores (__). They allow developers to define or customize the behavior of objects for built-in operations, such as initialization, representation, arithmetic operations, and more.

`Common Dunder Methods:`

- __init__: Constructor method called when an object is instantiated.
- __str__: Defines the string representation of the object (used by print()).
- __repr__: Defines the official string representation of the object (used in debugging).
- __len__: Defines behavior for the len() function.
- __eq__: Defines behavior for the equality operator ==.
- __add__: Defines behavior for the addition operator +.

`Program Example Incorporating Dunder Methods:`

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(f"{self.title} & {other.title}", self.author, self.pages + other.pages)
        return NotImplemented

# Usage
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)
book3 = Book("1984", "George Orwell", 328)

print(book1)              # Output: '1984' by George Orwell
print(repr(book1))        # Output: Book(title='1984', author='George Orwell', pages=328)
print(len(book1))         # Output: 328
print(book1 == book3)     # Output: True
print(book1 == book2)     # Output: False

combined_book = book1 + book2
print(combined_book)      # Output: '1984 & Animal Farm' by George Orwell
print(len(combined_book)) # Output: 440
```

`Explanation:`

- __str__: Provides a user-friendly string representation.
- __repr__: Provides a detailed string representation useful for debugging.
- __len__: Allows using len() to get the number of pages.
- __eq__: Enables comparison between two Book objects using ==.
- __add__: Allows adding two Book objects to create a new combined Book.

### 9. What is Method Overriding and Method Overloading?

`Answer:`

- **Method Overriding**

`Definition:` Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass has the same name, return type, and parameters as the one in the superclass.

`Purpose:` To modify or extend the behavior of the inherited method.

`Program Example:`

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

# Usage
parent = Parent()
child = Child()

parent.greet()  # Output: Hello from Parent
child.greet()   # Output: Hello from Child
```

- **Method Overloading**

`Definition:` Method overloading refers to the ability to define multiple methods with the same name but different parameters within the same class. However, Python does not support traditional method overloading as seen in languages like Java or C++. Instead, default arguments or variable-length arguments are used to achieve similar behavior.

`Program Example Using Default Arguments:`

```python
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

# Usage
math_op = MathOperations()
print(math_op.add(2, 3))      # Output: 5
print(math_op.add(2, 3, 4))   # Output: 9
```

`Program Example Using Variable-Length Arguments:`

```python
class MathOperations:
    def add(self, *args):
        return sum(args)

# Usage
math_op = MathOperations()
print(math_op.add(1, 2))           # Output: 3
print(math_op.add(1, 2, 3, 4, 5))  # Output: 15
```

`Note:` While Python does not support traditional method overloading, using default parameters or variable-length arguments can mimic this behavior.

### 10. What is Multiple Inheritance? Discuss its Advantages and Disadvantages?

`Answer:`

Multiple Inheritance is a feature in OOP where a class (subclass) can inherit attributes and methods from more than one parent class (superclass). This allows the subclass to combine behaviors from multiple sources.

`Program Example:`

```python
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

# Usage
donald = Duck()
donald.fly()    # Output: Flying
donald.swim()   # Output: Swimming
donald.quack()  # Output: Quack!
```

**`Advantages:`**

- `Code Reusability:` Combines functionalities from multiple classes without duplicating code.

- `Flexibility:` Allows a class to exhibit behaviors from different domains.

- `Modeling Complex Relationships:` Useful for modeling real-world scenarios where an entity may have multiple roles.

**`Disadvantages:`**

- `Complexity:` Can lead to more complex class hierarchies that are harder to understand and maintain.

- `Ambiguity:` Potential for the "Diamond Problem," where the inheritance hierarchy can cause ambiguity in method resolution.

- `Tight Coupling:` Classes become dependent on multiple parents, which can reduce modularity.

`Example of Diamond Problem:`

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

# Usage
d = D()
d.method()  # Output: Method in B
```

`Explanation:` In the above example, class D inherits from both B and C, which in turn inherit from A. When d.method() is called, Python's Method Resolution Order (MRO) determines which method to execute, resolving ambiguity by following a specific order (left-to-right depth-first).

### 11. Explain the super() Function in Python?

`Answer:`

The super() function in Python returns a temporary object of the superclass that allows you to call its methods. It is commonly used to extend the functionality of inherited methods without explicitly referring to the parent class.

`Benefits of Using super():`

- `Maintainability:` Makes code easier to maintain, especially in multiple inheritance scenarios.

- `Avoids Hardcoding Parent Class Names:` Prevents issues if the superclass name changes.

`Program Example:`

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Initialize superclass attributes
        self.breed = breed

    def speak(self):
        super().speak()        # Call superclass method
        print(f"{self.name} says Woof!")

# Usage
dog = Dog("Buddy", "Golden Retriever")
dog.speak()
# Output:
# Animal speaks.
# Buddy says Woof!
```

`Explanation:`

- super().__init__(name): Calls the __init__ method of the superclass Animal to initialize the name attribute.
= super().speak(): Calls the speak method of the superclass before adding additional behavior.

### 12. What is Composition vs. Inheritance?

`Answer:`

Both Composition and Inheritance are mechanisms to reuse code and establish relationships between classes in OOP, but they do so in different ways.

- `Inheritance`

`Definition:` Establishes an "is-a" relationship between classes.

`Usage:` When a class (subclass) needs to inherit attributes and behaviors from another class (superclass).

`Example:` A Car is a Vehicle.

`Program Example:`

```python
class Engine:
    def start(self):
        print("Engine started.")

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        self.engine = Engine()  # Composition

    def start_car(self):
        self.engine.start()
        print("Car started.")

# Usage
my_car = Car("Toyota")
my_car.start_car()
# Output:
# Engine started.
# Car started.
```

`Composition`

`Definition:`Establishes a "has-a" relationship between classes.

`Usage:` When a class (container) contains objects of other classes (components) to delegate responsibilities.

`Example:` A Car has an Engine.

`Program Example:`

```python
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()  # Composition

    def start_car(self):
        self.engine.start()
        print(f"{self.brand} car started.")

# Usage
my_car = Car("Honda")
my_car.start_car()
# Output:
# Engine started.
# Honda car started.
```

`Comparison:`

|   Aspect     | Inheritance   | Composition   |
|-------------:|--------------:|--------------:|
|Relationship  |    "Is-a"     |"Has-a"0       |
|  Coupling    |Tight coupling |Loose coupling |
|  Reusability |    High (inherits all public features) |  High (can selectively use features) |
|  Flexibility |    Less flexible, harder to change |  More flexible, easier to modify |
|  Hierarchical|    Yes |  No |

`When to Use:`

- `Inheritance:` When there's a clear hierarchical relationship and you want to reuse behavior from the parent class.

- `Composition:` When you want to build complex types by combining objects of other types, promoting flexibility and reusability.

### 13. How Does Python Handle Private and Protected Members?

`Answer:`

Python does not enforce access modifiers as strictly as languages like Java or C++. Instead, it relies on naming conventions to indicate the intended level of access for class members.

**Access Levels:**

1. `Public Members:`

`Definition:` Accessible from anywhere.

`Naming Convention:` No leading underscores.

`Example:`

```python
class MyClass:
    def __init__(self):
        self.public_attr = "I am public"

obj = MyClass()
print(obj.public_attr)  # Accessible
```

2. `Protected Members:`

`Definition:` Intended to be accessible within the class and its subclasses.

`Naming Convention:` Single leading underscore (_).

`Example:`

```python
class MyClass:
    def __init__(self):
        self._protected_attr = "I am protected"

class SubClass(MyClass):
    def access_protected(self):
        print(self._protected_attr)

obj = SubClass()
obj.access_protected()     # Accessible within subclass
print(obj._protected_attr) # Accessible but discouraged
```

3. `Private Members:`

`Definition:` Intended to be inaccessible from outside the class.

`Naming Convention:` Double leading underscores (__).

`Example:`

```python
class MyClass:
    def __init__(self):
        self.__private_attr = "I am private"

    def get_private_attr(self):
        return self.__private_attr

obj = MyClass()
# print(obj.__private_attr)  # AttributeError
print(obj.get_private_attr())  # Accessible via public method
```

`Name Mangling:` Python performs name mangling for private members to prevent accidental access.

```python
class MyClass:
    def __init__(self):
        self.__private_attr = "I am private"

obj = MyClass()
print(obj._MyClass__private_attr)  # Accessing via name mangling
```

### 14. What is the Difference Between __str__ and __repr__ Methods?

`Answer:`

Both __str__ and __repr__ are special methods (dunder methods) in Python used to define the string representation of an object. However, they serve different purposes and are used in different contexts.

`__str__ Method`

- `Purpose:` Provides a human-readable string representation of an object. It's intended for end-users.

- `Usage:` Called by the str() function and by the print() function.

- `Fallback:` If __str__ is not defined, Python uses __repr__.

`Example:`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Usage
person = Person("Alice", 30)
print(person)  # Output: Alice, 30 years old
```

`__repr__ Method`

- `Purpose:` Provides an official string representation of an object, which can be used to recreate the object if possible. It's intended for developers.

- `Usage:` Called by the repr() function and in interactive shells.

- `Fallback:` If __repr__ is not defined, Python uses the default implementation, which includes the object's memory address.

`Example:`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Usage
person = Person("Alice", 30)
print(repr(person))  # Output: Person(name='Alice', age=30)
```

`Combined Example:`

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

# Usage
book = Book("1984", "George Orwell")
print(str(book))   # Output: '1984' by George Orwell
print(repr(book))  # Output: Book(title='1984', author='George Orwell')
```

`Key Differences:`

- __str__ is for a readable representation, suitable for display to end-users.

- __repr__ is for an unambiguous representation, suitable for debugging and development.

### Design a simple Library Management System using Object-Oriented Programming principles. Your system should manage books and patrons (library members), allowing patrons to borrow and return books. Include basic functionalities such as adding new books, registering patrons, and tracking borrowed books.

**Approach:** To solve this, we'll identify the main classes and their relationships:

- `Book:` Represents a book in the library.

- `Patron:` Represents a library member.

- `Library:` Manages books and patrons, and handles the borrowing and returning of books.

`Class Design:`

1. **Book**

  - `Attributes:` title, author, isbn, is_borrowed

  - `Methods:` borrow(), return_book()

2. **Patron**

  - `Attributes:` name, patron_id, borrowed_books

  - `Methods:` borrow_book(book), return_book(book)

3. **Library**

  - **Attributes:** books, patrons

  - **Methods:** add_book(book), register_patron(patron), borrow_book(patron_id, isbn), return_book(patron_id, isbn)

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Book '{self.title}' has been borrowed.")
        else:
            print(f"Book '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Book '{self.title}' has been returned.")
        else:
            print(f"Book '{self.title}' was not borrowed.")


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"Cannot borrow '{book.title}'; it's already borrowed.")
        else:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")


class Library:
    def __init__(self):
        self.books = {}      # Key: ISBN, Value: Book instance
        self.patrons = {}    # Key: Patron ID, Value: Patron instance

    def add_book(self, book):
        if book.isbn in self.books:
            print(f"Book with ISBN {book.isbn} already exists.")
        else:
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added to the library.")

    def register_patron(self, patron):
        if patron.patron_id in self.patrons:
            print(f"Patron ID {patron.patron_id} already registered.")
        else:
            self.patrons[patron.patron_id] = patron
            print(f"Patron '{patron.name}' registered with ID {patron.patron_id}.")

    def borrow_book(self, patron_id, isbn):
        if patron_id not in self.patrons:
            print(f"Patron ID {patron_id} not found.")
            return
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[isbn]
        patron.borrow_book(book)

    def return_book(self, patron_id, isbn):
        if patron_id not in self.patrons:
            print(f"Patron ID {patron_id} not found.")
            return
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[isbn]
        patron.return_book(book)


# Example Usage:
if __name__ == "__main__":
    # Initialize library
    library = Library()

    # Add books
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    library.add_book(book1)
    library.add_book(book2)

    # Register patrons
    patron1 = Patron("Alice Smith", "P001")
    patron2 = Patron("Bob Johnson", "P002")
    library.register_patron(patron1)
    library.register_patron(patron2)

    # Borrow and return books
    library.borrow_book("P001", "1234567890")  # Alice borrows "1984"
    library.borrow_book("P002", "1234567890")  # Bob tries to borrow "1984"
    library.return_book("P001", "1234567890")  # Alice returns "1984"
    library.borrow_book("P002", "1234567890")  # Bob borrows "1984"
```

## Modules-and-Packages

### 1. What is a Python module?

`Answer:`

A Python module is a single file (with a .py extension) containing Python code, such as functions, classes, variables, and runnable code. Modules allow for code reuse and better organization by grouping related functionalities together.

`Example: Creating and Using a Module`

**Creating a Module (`math_utils.py`):**

```python
# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**Using the Module (`main.py`):**

```python
# main.py

import math_utils

result_add = math_utils.add(5, 3)
result_subtract = math_utils.subtract(5, 3)

print(f"Addition: {result_add}")         # Output: Addition: 8
print(f"Subtraction: {result_subtract}") # Output: Subtraction: 2
```

### 2. How do you import a specific function from a module?

`Answer:`

You can import specific functions from a module using the from keyword followed by the module name and the import statement.

`Example:`

**Module (`string_utils.py`):**

```python
# string_utils.py

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()
```

**Using Specific Function (`main.py`):**

```python
# main.py

from string_utils import to_uppercase

result = to_uppercase("hello")
print(result)  # Output: HELLO
```

### 3. How Many Modules Are There in Python?

`1. Built-in (Standard Library) Modules:`

Python comes with a vast standard library that includes a wide range of built-in modules. As of Python 3.11, there are over 200 built-in modules covering various functionalities such as:

- **File I/O and OS Interaction:** `os`, `sys`, `io`, `pathlib`

- **Data Types and Structures:** `math`, `datetime`, `json`, `collections`

- **Internet and Web Services:** `http`, `urllib`, `socket`, `email`

- **Concurrency and Parallelism:** `threading`, `multiprocessing`, `asyncio`

- **Testing and Debugging:** `unittest`, `doctest`, `pdb`

- **Others:** `random`, `re`, `logging`, `itertools`, `functools`

`2. Third-Party Modules:`

In addition to the standard library, Python has an extensive ecosystem of third-party modules available through the Python Package Index (PyPI). As of now, there are millions of third-party modules covering virtually every domain imaginable, such as:

- **Web Development:** `Django`, `Flask`, `FastAPI`

- **Data Science and Machine Learning:** `numpy`, `pandas`, `scikit-learn`, `tensorflow`

- **Visualization:** `matplotlib`, `seaborn`, `plotly`

- **Automation and Scripting:** `requests`, `beautifulsoup4`, `selenium`

- **Game Development:** `pygame`, `panda3d`

`Example:`

**`requests` Module:** Simplifies HTTP requests.

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # Output: 200
```

`3. Custom Modules:`

Beyond built-in and third-party modules, developers can create their own custom modules tailored to their specific needs. These modules are created by writing Python files and can be organized into packages for larger projects.

`Example:`

**Creating a custom module named `utilities.py`:**

```python
# utilities.py

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"
```

**Using the custom module in another script:**

```python
# main.py

import utilities

print(utilities.greet("Sam"))    # Output: Hello, Sam!
print(utilities.farewell("Ram"))   # Output: Goodbye, Ram!
```

### 4. Creating Your Own Modules

**Creating a Module**

To create a module, simply create a Python file (.py) with your desired functions, classes, or variables.

`Example:` greetings.py

```python
# greetings.py

def say_hello(name):
    return f"Hello, {name}!"

def say_goodbye(name):
    return f"Goodbye, {name}!"
```

**Using Your Module**

Assuming greetings.py is in the same directory as your main script:

```python
# main.py

import greetings

print(greetings.say_hello("Alice"))      # Output: Hello, Alice!
print(greetings.say_goodbye("Bob"))      # Output: Goodbye, Bob!
```

Import Specific Functions

```python
from greetings import say_hello

print(say_hello("Charlie"))  # Output: Hello, Charlie!
```

**Import with Aliasing**

```python
import greetings as gr

print(gr.say_goodbye("Diana"))  # Output: Goodbye, Diana!
```

**Creating a Package**

A package is a directory containing multiple modules and a special __init__.py file.

`Directory Structure:`

```markdown
my_package/
    __init__.py
    module1.py
    module2.py
```

**__init__.py**


```python
# my_package/__init__.py

from .module1 import function_a
from .module2 import function_b
```

**Using the Package**

```python
import my_package

my_package.function_a()
my_package.function_b()
```

Alternatively, import specific functions:

```python
from my_package import function_a, function_b

function_a()
function_b()
```

**Best Practices for Modules and Packages**

- Naming Conventions: Use lowercase names for modules and packages. Use underscores for readability if needed.

- Avoid Circular Imports: Ensure that modules do not import each other in a circular manner, which can lead to import errors.

- Use __all__: Define __all__ in your modules to specify which attributes should be exported when import * is used.

```python
# greetings.py
__all__ = ['say_hello', 'say_goodbye']
```

### 5. What is pip?

pip is the package installer for Python. It allows you to install and manage additional libraries and dependencies that are not part of the Python standard library.

## Working with Files

### 1. What is a Context Manager in Python?

A context manager allows you to properly manage resources, like opening and closing files, by automatically handling setup and teardown operations using the with statement. The most common use case is file handling.

```python
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)
```

### 2. How do you read and write to a CSV file in Python?

Python provides the csv module to handle CSV files.

**Program: Reading a CSV File**

```python
import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

**Program: Writing to a CSV File**

```python
import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

### 3. How can you read and write JSON data in Python?

Python has the json module that allows for easy reading and writing of JSON data, which is a popular data interchange format.

**Program: Reading a JSON File**

```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
```

**Program: Writing a JSON File**

```python
import json

data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)
```

### 4. How can you read a CSV file into a dictionary in Python?

You can use the csv.DictReader to convert rows in a CSV file into dictionaries where the keys are the column headers.

**Program: Reading CSV into a Dictionary**

```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Each row is a dictionary
```

### 5. How can you write a dictionary to a CSV file in Python?

You can use csv.DictWriter to write dictionaries to a CSV file where each dictionary represents a row.

**Program: Writing Dictionary to CSV**

```python
import csv

data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
]

with open('output.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write the column headers
    writer.writerows(data)
```

### 6. What happens if you try to read from a file that does not exist?

If you try to open a file that does not exist, Python raises a `FileNotFoundError`.

```python
try:
    with open('non_existent_file.txt', 'r') as file:
        data = file.read()
except FileNotFoundError as e:
    print("Error: File not found!")
```

### 7. How do you handle file encoding while reading or writing a file in Python?

You can specify the encoding parameter in the open() function to handle different text encodings (`like UTF-8 or ISO-8859-1`).

```python
with open('example.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)
```

### 8. How do you append data to an existing file?

To append data to a file, you open it in append mode (`a`), which ensures new data is added to the end of the file without overwriting its current contents.

```python
with open('example.txt', 'a') as file:
    file.write("This is additional text.\n")
```

### 9. What are the different file modes available in Python’s open() function?

- `r`: Read (default mode)

- `w`: Write (truncates the file if it exists)

- `a`: Append

- `x`: Create a new file, but fail if it already exists

- `b`: Binary mode

- `t`: Text mode (default)

### 10.How would you handle large files that don't fit into memory in Python?

For large files, you can read or write them line by line to avoid memory issues.

**Program: Reading a File Line by Line**

```python
with open('large_file.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

### 11. Merging Two CSV Files

```python
import csv

with open('file1.csv', 'r') as f1, open('file2.csv', 'r') as f2, open('merged.csv', 'w', newline='') as fout:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    writer = csv.writer(fout)
    
    # Write headers from the first file
    writer.writerows(reader1)
    
    # Skip header of the second file
    next(reader2)
    
    # Write the rows of the second file
    writer.writerows(reader2)
```

## Decorators and Generators

### 1. What is a Python decorator, and how is it used?

A decorator in Python is a function that modifies or extends the behavior of another function or method without altering the actual code of the function being decorated. It takes a function as an argument and returns a new function that enhances the original one.

```python
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def greet():
    print("Hello, World!")

# Call the decorated function
greet()

# output

# Before the function call
# Hello, World!
# After the function call
```

### 2. Can you explain the difference between @staticmethod and @classmethod?

- `@staticmethod:` A static method does not receive an implicit first argument (like self or cls). It behaves like a regular function but belongs to the class’s namespace.

- `@classmethod:` A class method receives the class (cls) as its first argument and can modify class-level data.

```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method, and we are in {cls.__name__} class.")

# Usage
MyClass.static_method()  # Call static method
MyClass.class_method()   # Call class method

# output

# This is a static method.
# This is a class method, and we are in MyClass class.
```

### 3. What is a generator in Python? How does it work?

A generator in Python is a function that returns an iterator and produces values one at a time using the yield keyword. Unlike normal functions, which return all values at once, a generator suspends its state and resumes from where it left off on the next call.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Yield suspends the function and returns a value
        count += 1

# Usage of the generator
for number in count_up_to(5):
    print(number)

# output
# 1
# 2
# 3
# 4
# 5
```

### 4. What are the benefits of using generators over lists?

- `Memory Efficiency:` Generators yield one value at a time, which makes them more memory-efficient, especially with large datasets.

- `Lazy Evaluation:` Generators produce items only when needed, which can improve performance in certain situations.

- `Infinite Sequences:` Generators can represent infinite sequences, such as the Fibonacci sequence, without running out of memory.

### 5. Write a Python program that uses a generator to produce the Fibonacci sequence.

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create a generator for Fibonacci numbers
fib_gen = fibonacci()

# Get the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))
```

### 6. Can you create a decorator that counts how many times a function has been called?

Here’s a decorator that tracks the number of times a function is invoked

```python
def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1  # Increment the count each time the function is called
        print(f"Function '{func.__name__}' has been called {wrapper.count} times.")
        return func(*args, **kwargs)
    wrapper.count = 0  # Initialize the counter
    return wrapper

@call_counter
def say_hello():
    print("Hello!")

# Call the decorated function multiple times
say_hello()
say_hello()
say_hello()
```

### 7. What is the difference between return and yield?

- `return:` Exits the function and returns a value, after which the function is terminated.

- `yield:` Suspends the function’s state, returning a value temporarily. The function can later be resumed, continuing from where it left off.

### 8. Write a generator expression to create squares of numbers from 1 to 10.

```python
# Generator expression for squares
squares = (x * x for x in range(1, 11))

# Use the generator
for square in squares:
    print(square)
```

## Comprehensions

### 1. What are comprehensions in Python, and how are they used in lists, dictionaries, and sets? Could you write examples to demonstrate each type?

Comprehensions in Python provide a concise and efficient way to create collections (like lists, dictionaries, and sets) by iterating over an iterable and optionally applying conditions or transformations. They can replace verbose for-loops, making the code more readable and Pythonic.

**Types of Comprehensions:**

1. `List Comprehension:` A list comprehension is used to generate a list in a single line by applying expressions and conditions to each element of an iterable.

- Syntax: `[expression for item in iterable if condition]`

2. `Dictionary Comprehension:` A dictionary comprehension allows us to construct dictionaries by specifying key-value pairs directly in a loop-based format.

Syntax: `{key_expression: value_expression for item in iterable if condition}`

3. `Set Comprehension:` A set comprehension generates a set by applying transformations and conditions on an iterable.

Syntax: `{expression for item in iterable if condition}`

### 2 This simple program demonstrates list, dictionary, and set comprehensions.

```python
# List Comprehension: Create a list of squares from 0 to 9
squares_list = [x**2 for x in range(10)]
print(f"Squares List: {squares_list}")

# Dictionary Comprehension: Create a dictionary with numbers and their squares
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares Dictionary: {squares_dict}")

# Set Comprehension: Create a set of unique even numbers from 0 to 9
even_set = {x for x in range(10) if x % 2 == 0}
print(f"Even Set: {even_set}")
```

**Output:**

```yaml
Squares List: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Squares Dictionary: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
Even Set: {0, 2, 4, 6, 8}
```

### 3. This program demonstrates a more practical use of comprehensions: filtering and transforming data based on conditions.

```python
# Suppose we have a list of students and their marks
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 58},
    {"name": "Charlie", "marks": 90},
    {"name": "David", "marks": 47},
    {"name": "Eve", "marks": 76}
]

# 1. List Comprehension: Get a list of students who passed (marks >= 60)
passed_students = [student["name"] for student in students if student["marks"] >= 60]
print(f"Passed Students: {passed_students}")

# 2. Dictionary Comprehension: Create a dictionary of students and their grades based on marks
grades = {student["name"]: "A" if student["marks"] >= 85 else "B" if student["marks"] >= 60 else "C" for student in students}
print(f"Student Grades: {grades}")

# 3. Set Comprehension: Get a set of unique grades
unique_grades = {grade for grade in grades.values()}
print(f"Unique Grades: {unique_grades}")
```

**output**

```yaml
Passed Students: ['Alice', 'Charlie', 'Eve']
Student Grades: {'Alice': 'A', 'Bob': 'C', 'Charlie': 'A', 'David': 'C', 'Eve': 'B'}
Unique Grades: {'C', 'B', 'A'}
```

##  Regular Expressions (Regex)

### 1. What are regular expressions (regex) in Python, and how would you use them for pattern matching and substitution in strings? Could you write a Python program that performs the following tasks:

- Finds all occurrences of words starting with `a` in a string.

- Replaces every digit in the string with a `#` symbol.

`Answer:`

Regular expressions (regex) are sequences of characters that define search patterns, primarily for string pattern matching. In Python, the `re` module provides support for working with regex. It includes functions like `re.search()`, `re.match()`, `re.findall()`, and `re.sub()` to find and manipulate patterns in text.

- `Pattern Matching:` This involves searching for specific patterns in a string using functions like `re.search()` or `re.findall()`.

- `Substitution:` With `re.sub()`, you can replace 

`Program:`

Here’s a Python program that:

- Finds all words starting with `a`.

- Replaces all digits with `#`.

```python
import re

# Sample input string
input_string = "Alice is 24 years old, and her brother Adam is 17."

# Task 1: Find all words that start with the letter 'a' (case insensitive)
words_starting_with_a = re.findall(r'\b[aA]\w*\b', input_string)

print("Words starting with 'a':", words_starting_with_a)

# Task 2: Replace all digits with '#'
replaced_string = re.sub(r'\d', '#', input_string)

print("String after replacing digits:", replaced_string)
```

## Lambda Functions and Functional Programming

### 1. What is a lambda function in Python? Explain its syntax and when you would use it.

A lambda function in Python is an anonymous function defined with the `lambda` keyword. It can take any number of arguments but must contain a single expression. Lambda functions are typically used when a small, throwaway function is required, especially in higher-order functions like `map()`, `filter()`, or `reduce()`.

**Syntax:**

```python
lambda arguments: expression
```

**Example**

```python
# Lambda function to calculate square of a number
square = lambda x: x ** 2
print(square(4))  # Output: 16
```

### 2. What is the `map()` function in Python? Write a Python program to demonstrate its usage?

The `map()` function applies a specified function to each item of an iterable (like a list) and returns an iterator. You can use it to transform elements based on a function.

**Syntax:**

```python
map(function, iterable)
```

**Example**

```python
# Function to double a number
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
# Using map with a regular function
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10]

# Using lambda with map
doubled_lambda = map(lambda x: x * 2, numbers)
print(list(doubled_lambda))  # Output: [2, 4, 6, 8, 10]
```

### 3. How does the `filter()` function work in Python? Write a program to filter out even numbers from a list using both a regular function and a lambda function?

The `filter()` function applies a function to each element of an iterable and returns only the elements for which the function returns `True`. It's commonly used for filtering collections of data.

**Syntax:**

```python
filter(function, iterable)
```

**Example**

```python
# Function to check if a number is even
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

# Using filter with a regular function
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

# Using lambda with filter
even_lambda = filter(lambda x: x % 2 == 0, numbers)
print(list(even_lambda))  # Output: [2, 4, 6]
```

### 4. What is the `reduce()` function in Python, and how is it different from `map()`? Demonstrate its use with an example program that multiplies all numbers in a list?

The `reduce()` function, from the `functools` module, applies a rolling computation to pairs of elements in an iterable, reducing it to a single cumulative value. Unlike `map()`, which returns a new iterable,`reduce()` returns a single value.

**Syntax:**

```python
from functools import reduce
reduce(function, iterable)
```

**Example**

```python
from functools import reduce

# Function to multiply two numbers
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]

# Using reduce with a regular function
product = reduce(multiply, numbers)
print(product)  # Output: 120

# Using lambda with reduce to achieve the same result
product_lambda = reduce(lambda x, y: x * y, numbers)
print(product_lambda)  # Output: 120
```

### 5. Write a Python program that uses `map()`, `filter()`, and `reduce()` together. Use these to find the product of all even numbers in a list of integers?

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Use filter() to get only the even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Step 2: Use map() to square the even numbers
squared_evens = map(lambda x: x ** 2, even_numbers)

# Step 3: Use reduce() to find the product of all squared even numbers
product_of_squares = reduce(lambda x, y: x * y, squared_evens)

print(product_of_squares)  # Output: 576  (i.e., 2^2 * 4^2 * 6^2 = 576)
```

### 6. What is the main difference between map`()` and `filter()` in Python?

- `map()` applies a function to all items in an iterable and returns a new iterable with the transformed items.

- `filter()` applies a function that returns True or False to each item in an iterable, and only the items that evaluate to True are included in the result.

Both functions return iterators, but `map()` transforms all items while `filter()` selectively removes items based on a condition.

## Error Handling (Advanced)

### 1. What are custom exceptions in Python, and how do you define and use them?

Custom exceptions in Python allow developers to create specific exceptions for their application. This makes error handling more meaningful by reflecting domain-specific errors rather than relying on generic built-in `exceptions` like `ValueError` or `TypeError`. Custom exceptions are defined by creating a new class that inherits from the built-in Exception class or one of its subclasses. You can add custom attributes and messages to provide more context when the exception is raised.

### 2. How do you raise exceptions in Python? Can you raise both built-in and custom exceptions?

In Python, you can raise exceptions using the raise keyword. You can raise both built-in exceptions like ValueError, TypeError, etc., or custom exceptions that you’ve defined. Raising exceptions allows you to signal that an error has occurred in your code, even if no natural exception is thrown.

**Example Program: Custom Exceptions and Raising Exceptions**

```python
# Defining a custom exception for invalid age
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age is not valid. It must be between 0 and 120."):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Defining another custom exception for negative withdrawals
class NegativeWithdrawalError(Exception):
    def __init__(self, amount, message="Withdrawal amount cannot be negative"):
        self.amount = amount
        self.message = message
        super().__init__(self.message)

# Function to set age with custom exception handling
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to {age}")

# Function to withdraw money with custom exception handling
def withdraw(amount, balance):
    if amount < 0:
        raise NegativeWithdrawalError(amount)
    if amount > balance:
        raise ValueError("Cannot withdraw more than the available balance")
    balance -= amount
    return balance

# Main block to test custom exceptions
try:
    # Test setting an invalid age
    set_age(150)
except InvalidAgeError as e:
    print(f"Error: {e.message} (Age provided: {e.age})")

try:
    # Test withdrawing a negative amount
    balance = withdraw(-50, 100)
except NegativeWithdrawalError as e:
    print(f"Error: {e.message} (Amount provided: {e.amount})")

try:
    # Test withdrawing more than the balance
    balance = withdraw(200, 100)
except ValueError as e:
    print(f"Error: {e}")
```

### 3. Can custom exceptions inherit from exceptions other than `Exception`?

Yes, custom exceptions can inherit from any existing exception class, like `ValueError`, `TypeError`, etc., depending on the type of error you want to raise. However, the most common practice is to inherit from `Exception`.

### 4. How can you re-raise an exception after handling it?

You can re-raise an exception by using `raise` within an `except` block without specifying any arguments. This passes the exception up the call stack.

```python
try:
    # some code
    set_age(200)
except InvalidAgeError as e:
    print(f"Error logged: {e}")
    raise  # Re-raises the caught exception
```

## Unit Testing

### 1. What is Unit Testing, and why is it important?

Unit testing is a software testing technique where individual units or components of a program are tested in isolation. The purpose is to validate that each unit performs as expected. It's important because:

- It helps in identifying bugs early in the development process.

- It makes the code more reliable and easier to maintain.

- It encourages better code design and modularity.

- Unit tests can act as documentation for the behavior of the code.

### 2. What is the difference between unittest and pytest in Python?

- `unittest` is the built-in Python testing library. It follows a class-based approach to writing test cases and provides specific methods like `assertEqual`, `assertTrue`, and more.

- `pytest` is a more feature-rich and flexible testing framework. It uses a function-based approach, leveraging Python's `assert` statement. It also has advanced features like fixtures, parameterized tests, and easier integration with external libraries for test discovery, mocking, and test coverage.

`Key differences:`

- `pytest` uses simpler syntax and does not require you to write a class or methods.

- `pytest` offers more powerful fixtures and a flexible plugin system.

- `unittest` is part of the standard library, while `pytest` needs to be installed separately.

### 3. What are fixtures in testing, and how do they work in pytest?

Fixtures are functions that set up some precondition or state for the tests and clean up afterward. In `pytest`, fixtures are used to provide common setup code for multiple tests, which can be shared across different test functions.

In `pytest`, you use the `@pytest.fixture` decorator to mark a function as a fixture. The function can then be passed as an argument to test functions, and `pytest` will automatically inject the fixture when running the tests.

```python
@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_user_data(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30
```

### 4. What are the common assertions used in unittest?

Some common assertions in unittest include:

- `assertEqual(a, b):` Asserts that `a == b`.
- `assertNotEqual(a, b):` Asserts that `a != b`.
- `assertTrue(x):` Asserts that `x` is `True`.
- `assertFalse(x):` Asserts that `x` is `False`.
- `assertRaises(Exception, func, *args):` Asserts that a certain exception is raised during the execution of `func` with given `args`.
- `assertIn(item, container):` Asserts that `item` is in the `container`.
- `assertIsNone(x):` Asserts that `x` is `None`.

### 5. What is Test-Driven Development (TDD), and how does it relate to unit testing?

Test-Driven Development (TDD) is a software development approach in which tests are written before writing the actual code. The process follows three main steps:

- `Write a test:` Write a test that defines a function or improvements that should be made.
- `Run the test:` The test should initially fail, confirming that the function is not yet implemented or incorrect.
- `Write the code:` Implement the minimal amount of code required to pass the test.
- `Refactor the code:` Clean up the code while ensuring that the test continues to pass.

Unit testing is fundamental to TDD, as you rely on unit tests to define and verify the behavior of your functions step-by-step

### 6. Write unit tests for a function that checks whether a string is a palindrome?

**Problem:**

Write a function is_palindrome(s) that returns True if the input string s is a palindrome, ignoring spaces and capitalization. Then, write unit tests for this function using unittest.

**Solution:**

```python
# Function to check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Unit Test using unittest
import unittest

class TestPalindrome(unittest.TestCase):
    
    def test_palindrome(self):
        # Test positive cases
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        
        # Test negative cases
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        
        # Test edge cases
        self.assertTrue(is_palindrome(""))  # Empty string
        self.assertTrue(is_palindrome("a"))  # Single character
        
if __name__ == '__main__':
    unittest.main()
```

### 7. Write a parameterized test using `pytest` for a function that multiplies two numbers.

**Problem:**

Create a function `multiply(a, b)` that returns the product of `a` and `b`. Then, write parameterized tests for the function using `pytest`.

**Solution:**

```python
# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Pytest - Parameterized Test
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),      # Positive numbers
    (-1, 5, -5),    # Negative and positive
    (0, 100, 0),    # Zero multiplied by a number
    (-3, -7, 21),   # Two negative numbers
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
```

### 8. Write unit tests to check if a function raises a `ValueError` when given invalid input.

**Problem:**

Create a function `divide(a, b)` that divides two numbers, but raises a `ValueError` if the divisor is zero. Write unit tests using `unittest` to check for the `ValueError`.

**Solution:**

```python
# Function to divide two numbers
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Unit Test using unittest
import unittest

class TestDivision(unittest.TestCase):
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, 3), -2)
    
    def test_divide_by_zero(self):
        # Check for ValueError when dividing by zero
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```
