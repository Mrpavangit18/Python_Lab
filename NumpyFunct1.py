# Task 1: Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions.
#         Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 
#         Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
import numpy as np

# Given temperature data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Find hot days (temperature > 35°C)
hot_days_indices = np.where(temperatures > 35)[0]
hot_days_temperatures = temperatures[hot_days_indices]

# Find cold days (temperature < 5°C)
cold_days_indices = np.where(temperatures < 5)[0]
cold_days_temperatures = temperatures[cold_days_indices]

# Print the results
print("Hot Days:")
print("Day   Temperature (C)")
for day, temp in zip(hot_days_indices, hot_days_temperatures):
    print(f"{day + 1:2d}      {temp:.1f}")

print("\nCold Days:")
print("Day   Temperature (°C)")
for day, temp in zip(cold_days_indices, cold_days_temperatures):
    print(f"{day + 1:2d}      {temp:.1f}")
    

"""
Hot Days:
Day   Temperature (C)
 3       36.8
 6       38.7
10      37.2

Cold Days:
Day   Temperature (°C)
11      4.0
14     -4.0
15    -12.0
"""
