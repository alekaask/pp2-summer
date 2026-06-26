# This script shows how to use enumerate() and zip() for paired iteration.

items = ["apple", "banana", "cherry"]
for index, item in enumerate(items):
    print(index, item)

# Expected output:
# 0 apple
# 1 banana
# 2 cherry

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)

# Expected output:
# Alice 25
# Bob 30
# Charlie 35

# Type checking and conversions.
value = "10"
print(type(value))
print(int(value))
print(type(int(value)))

# Expected output:
# <class 'str'>
# 10
# <class 'int'>
