# Task 2: Compute the standard deviation of the NumPy array
#         Input: arr = [20, 2, 7, 1, 34]

import numpy as np

arr = [20, 2, 7, 1, 34]

# Convert the list to a NumPy array
arr = np.array(arr)

# Calculate the standard deviation
std_dev = np.std(arr)

print("Standard deviation:", std_dev)

# Output:
# Standard deviation: 12.576167937809991
