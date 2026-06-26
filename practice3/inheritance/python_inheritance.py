# Example 1: A child class inherits from a parent class.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

# Expected output:
# Mike Olsen

# Example 2: Method overriding in a child class.
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

animal = Dog()
animal.sound()

# Expected output:
# Bark

# Example 3: Using super() in the child class constructor.
class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

m = Manager("Sara", "Sales")
print(m.name, m.department)

# Expected output:
# Sara Sales

# Example 4: Using super() inside a method.
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c = Child()
c.greet()

# Expected output:
# Hello from Parent
# Hello from Child
