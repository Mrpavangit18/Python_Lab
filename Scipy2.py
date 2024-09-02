# Task 2: Using SciPy Linear Algebra please solve the below problem. Input: 7x + 2y = 8 4x + 5y = 10

# Import necessary libraries
import numpy as np
from scipy import linalg

# Define the coefficients of the equations
# Coefficients of the variables in the equations
a = np.array([[7, 2], [4, 5]])

# Constants on the right-hand side of the equations
b = np.array([8, 10])

# Solve the system of equations
solution = linalg.solve(a, b)

# Print the solution
print("Solution:")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")

# Output:
# Solution:
# x = 0.7407407407407407
# y = 1.4074074074074074
