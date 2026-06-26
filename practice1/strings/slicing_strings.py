#characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])
#output: llo

#slice from the start to position 5 (not included)
b = "Hello, World!"
print(b[:5])
#output: Hello

#slice to the end of the string
b = "Hello, World!"
print(b[2:])
#output: llo, World!

#negative indexing means starting from the end of the string
b = "Hello, World!"
print(b[-5:-2])
#output: orl