# Task 1:

import matplotlib.pyplot as plt

# Data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create a pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140)

# Add a title
plt.title('Monthly Income Distribution by Source')

# Display the pie chart
plt.show()
