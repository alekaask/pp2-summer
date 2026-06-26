# This script shows that comparison operators return True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Expected output:
# True
# False
# False

# This example uses an if/else block to print a message based on a condition.
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Expected output:
# b is not greater than a

# The bool() function converts values into a boolean result.
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Expected output:
# True
# True
# True
# True

# Many values are considered True unless they are empty or zero-like.
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Expected output:
# True
# True
# True

# These values evaluate to False in Python.
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Expected output:
# False
# False
# False
# False
# False
# False
# False

# A class with __len__ returning 0 is treated as False.
class MyClass:
    def __len__(self):
        return 0

myobj = MyClass()
print(bool(myobj))

# Expected output:
# False

# Functions can return booleans and be used in conditions.
def my_function():
    return True

print(my_function())

def my_function2():
    return True

if my_function2():
    print("YES!")
else:
    print("NO!")

# Expected output:
# True
# YES!

# isinstance() checks whether an object is a specific type.
x = 200
print(isinstance(x, int))

# Expected output:
# True
