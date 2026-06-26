print("Hello")
print('Hello')

#quotes inside quotes
print("It's a beautiful day")
print("He is called 'Johnny'")

#assign string to a variable
a = "Hello"
print(a)

#you can use three double quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings are arrays
a = "Hello, World!"
print(a[1])

#looping through a string
for x in "banana":
  print(x)

#string length: the length of a string through len() function
a = "Hello, World!"
print(len(a))

#check string: to check if a certain phrase or character is present in a string, we can use the keyword in
txt = "The best things in life are free!"
print("free" in txt)

#print only if free in txt
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#check if not: to check if a certain phrase or character is NOT present in a string, we can use the keyword not in
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")