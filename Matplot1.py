# Task 1: Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 
"""
Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 

# Monthly expenses in dollars (replace with your own data) 

expenses = [1200, 400, 200, 150, 250]"""

import matplotlib.pyplot as plt

# Categories and corresponding expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]  # Replace with your own data

# Create the bar chart
plt.figure(figsize=(10, 6))  # Set the size of the figure
plt.bar(categories, expenses, color='skyblue')  # Create a bar chart with skyblue bars
plt.xlabel('Categories')  # Label for the x-axis
plt.ylabel('Expenses ($)')  # Label for the y-axis
plt.title('Monthly Expenses by Category')  # Title of the chart
plt.show()  # Display the chart
