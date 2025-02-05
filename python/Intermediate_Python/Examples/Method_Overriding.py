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