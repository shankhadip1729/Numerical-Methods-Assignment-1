L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0

for i, num in enumerate(L):
    if 2 ** X == num:
        print(f"{2**X} is at index {i}")
        break
else:
    print(f"{X} not found")