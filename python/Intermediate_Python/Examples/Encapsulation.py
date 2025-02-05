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