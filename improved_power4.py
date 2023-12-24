
X = 5
L = [2 ** i for i in range(7)]
print("Generated powers-of-2 list:",L)

target_value = 2 ** X

if target_value in L:
    print(f"{2**X} at index {L.index(target_value)}")
else:
    print(f"{X} not found")