# Pavan Deore
# Task 1: Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

# Creating an array of 10 zeros
zeros_array = np.zeros(10)
print("An array of 10 zeros:")
print(zeros_array)

# Creating an array of 10 ones
ones_array = np.ones(10)
print("An array of 10 ones:")
print(ones_array)

# Creating an array of 10 fives
fives_array = np.ones(10) * 5
print("An array of 10 fives:")
print(fives_array)


# Output:
"""
An array of 10 zeros:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
An array of 10 ones:
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
An array of 10 fives:
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.] """
