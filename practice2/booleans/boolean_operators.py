# This script demonstrates boolean operators with simple comparisons.
x = 5

# and requires both conditions to be True.
print(x > 3 and x < 10)
print(x > 3 and x < 4)

# Expected output:
# True
# False

# or requires at least one condition to be True.
print(x > 3 or x < 4)
print(x > 3 or x < 2)

# Expected output:
# True
# True

# not reverses the boolean result.
print(not(x > 3 and x < 10))
print(not(x > 3 and x < 4))

# Expected output:
# False
# True
