# Task 1: Install matplotlib  & you can use plt.plot() to create a line plot of given data
# x = [0, 5, 9, 10, 15, 20, 25] 
# y = [0, 1, 2, 3, 4, 5, 6]

import matplotlib.pyplot as plt

x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()

# Output:
# Output is shown in image file
