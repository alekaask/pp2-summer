#many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#output: Orange
#output: Banana
#output: Cherry

#one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#output: Orange
#output: Orange
#output: Orange

#unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)