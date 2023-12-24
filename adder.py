# adder_function.py

# Function to add two numbers
def adder(a, b):
    return a + b

# Call the function to add two strings, two lists, and two floating points
result_string = adder("Hello", "World")
result_list = adder([1, 2, 3], [4, 5, 6])
result_float = adder(3.14, 2.71)

# Print the results
print("Result of adding two strings:", result_string)
print("Result of adding two lists:", result_list)
print("Result of adding two floating points:", result_float)

# Generalized adder function to add an arbitrary number of arguments
def adder_general(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

# Test the generalized adder function with keyword arguments
result_general = adder_general(1, 2, 3, good=5, bad=2, ugly=1)

# Print the result
print("\nResult of generalized adder function:", result_general)
