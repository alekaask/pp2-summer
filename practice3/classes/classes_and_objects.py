# Example 1: Create a simple class and object.
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("John")
print(p1.name)

# Expected output:
# John

# Example 2: Add an instance method to a class.
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()

# Expected output:
# Woof!

# Example 3: Use attributes inside a method.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

cat1 = Cat("Milo", 2)
cat1.info()

# Expected output:
# Milo 2

# Example 4: Change an object's attribute after creation.
class Book:
    def __init__(self, title):
        self.title = title

book1 = Book("Python Basics")
book1.title = "Advanced Python"
print(book1.title)

# Expected output:
# Advanced Python
