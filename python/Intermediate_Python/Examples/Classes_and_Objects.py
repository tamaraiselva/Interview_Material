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