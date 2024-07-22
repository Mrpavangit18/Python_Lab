# Pavan Deore
# Task 2: Convert the below list into a numpy array then display the array then display the first and last index and
#         then multiply each element by 2 and display the result.
#         Input: my_list = [1, 2, 3, 4, 5]

# Program:
import numpy as np

my_list = [1, 2, 3, 4, 5]
numpy_array = np.array(my_list)

print("NumPy array:")
print(numpy_array)

# First and last elements
first_element = numpy_array[0]
last_element = numpy_array[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")

# Multiply each element by 2
doubled_array = numpy_array * 2
print("Doubled array:")
print(doubled_array)

# Output:
"""
NumPy array:
[1 2 3 4 5]
First element: 1
Last element: 5
Doubled array:
[ 2  4  6  8 10]
"""
