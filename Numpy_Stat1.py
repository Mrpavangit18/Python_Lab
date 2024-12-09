# Task 1: Compute the median of the flattened NumPy array 
#         Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

import numpy as np

x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# Print the original array
print("Printing the Original array:", x_odd)

# Calculate the median of the flattened array
median_value = np.median(x_odd)

print("Median of the array:", median_value)


# Output:
#Printing the Original array: [1 2 3 4 5 6 7]
# Median of the array: 4.0
