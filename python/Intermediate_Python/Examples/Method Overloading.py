class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

# Usage
math_op = MathOperations()
print(math_op.add(2, 3))      # Output: 5
print(math_op.add(2, 3, 4))   # Output: 9


class MathOperations:
    def add(self, *args):
        return sum(args)

# Usage
math_op = MathOperations()
print(math_op.add(1, 2))           # Output: 3
print(math_op.add(1, 2, 3, 4, 5))  # Output: 15