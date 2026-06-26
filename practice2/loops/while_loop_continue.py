# This loop skips the current iteration when continue is used.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Expected output:
# 1
# 2
# 4
# 5
# 6
