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