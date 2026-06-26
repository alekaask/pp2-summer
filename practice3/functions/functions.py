# Example 1: A function with one parameter.
def greet(name):
    print("Hello, " + name)

greet("Alice")

# Expected output:
# Hello, Alice

# Example 2: A function that returns a value.
def add(a, b):
    return a + b

print(add(3, 4))

# Expected output:
# 7

# Example 3: A function with a default parameter.
def welcome(name="Student"):
    print("Welcome, " + name)

welcome()
welcome("Bob")

# Expected output:
# Welcome, Student
# Welcome, Bob

# Example 4: A function with keyword arguments.
def describe_pet(name, kind):
    print(name + " has a " + kind)

describe_pet(kind="dog", name="Max")

# Expected output:
# Max has a dog
