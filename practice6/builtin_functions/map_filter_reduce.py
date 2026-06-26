# This script demonstrates map(), filter(), and reduce() on lists.
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Use map() to square each number.
squared = list(map(lambda x: x * x, numbers))
print("Squared:", squared)

# Use filter() to keep only even numbers.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Use reduce() to calculate the sum of all values.
total = reduce(lambda x, y: x + y, numbers)
print("Total:", total)

# Expected output:
# Squared: [1, 4, 9, 16, 25]
# Even numbers: [2, 4]
# Total: 15
