# This loop skips one item and continues with the next one.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Expected output:
# apple
# cherry
