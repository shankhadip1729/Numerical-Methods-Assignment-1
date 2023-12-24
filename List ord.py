S = 'mumbai'

# Task 1: Print each character and its Unicode code point using a for loop
print("Task 1:")
for char in S:
    code_point = ord(char)
    print(f"Character: {char}, Unicode Code Point: {code_point}")

# Task 2: Compute the sum of Unicode code points
print("\nTask 2:")
unicode_sum = 0
for char in S:
    unicode_sum += ord(char)
print(f"Sum of Unicode Code Points: {unicode_sum}")

# Task 3: Return a list of Unicode code points in three ways

# 3.1 Using list methods
unicode_list_method = list(map(ord, S))
print("\nTask 3.1:")
print("Unicode Code Points (using list methods):", unicode_list_method)

# 3.2 Using list comprehension
unicode_list_comprehension = [ord(char) for char in S]
print("\nTask 3.2:")
print("Unicode Code Points (using list comprehension):", unicode_list_comprehension)

# 3.3 Using the map class
unicode_map_class = list(map(ord, S))
print("\nTask 3.3:")
print("Unicode Code Points (using map class):", unicode_map_class)
