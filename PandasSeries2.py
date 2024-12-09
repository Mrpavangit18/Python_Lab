# Task 2: import pandas as pd

# Expense categories
# categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Monthly expense data (example data in USD)
# expenses = [500, 200, 1200, 300, 150]

# Creating a Pandas Series to represent the expenses
# expenses_series = pd.Series(data=expenses, index=categories)

# Display the Pandas Series
# print(expenses_series)

import pandas as pd

# Expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Monthly expense data (example data in USD)
expenses = [500, 200, 1200, 300, 150]

# Creating a Pandas Series to represent the expenses
expenses_series = pd.Series(data=expenses, index=categories)

# Display the Pandas Series
print(expenses_series)

# Output:
"""
Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
dtype: int64
"""

