x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

#int is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#float is a floating number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#complex numbers are written with a "j" as the imaginary part.
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#also you can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))