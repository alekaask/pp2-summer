# This script uses shorthand if/else syntax for compact conditional expressions.
a = 330
b = 330

print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

# Expected output:
# B
# =
