L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0

while i < len(L):
    if 2 ** X == L[i]:
        found = True
        print(f"{2**X} is at {i}")
        break
    i += 1
else:
    print(f"{X} not found")