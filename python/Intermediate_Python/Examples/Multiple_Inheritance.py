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


#--------------Diamond Problem----------

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