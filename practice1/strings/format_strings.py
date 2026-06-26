#string format: we cannot combine strings and numbers like this:
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

#f-strings: we can combine strings and numbers like this:
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#output: My name is John, I am 36

#placeholder: we can combine strings and numbers like this:
age = 36
txt = "My name is John, I am {age:.2f}"
print(txt)
#output: My name is John, I am 36.00

#perform a math operations
txt = f"The price is {20 * 59} dollars"
print(txt)