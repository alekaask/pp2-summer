# Example 1: Lambda with map() to square numbers.
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)

# Expected output:
# [1, 4, 9, 16]

# Example 2: Lambda with filter() to keep even numbers.
values = [1, 2, 3, 4, 5, 6]
even_values = list(filter(lambda x: x % 2 == 0, values))
print(even_values)

# Expected output:
# [2, 4, 6]

# Example 3: Lambda with sorted() to sort words by length.
words = ["apple", "kiwi", "banana", "pear"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)

# Expected output:
# ['kiwi', 'pear', 'apple', 'banana']

# Example 4: Lambda used in a small calculator-like function.
make_sum = lambda a, b: a + b
print(make_sum(7, 8))

# Expected output:
# 15
