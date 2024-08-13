# Task 2: rite a Pandas program to create a Pivot table and find the item wise unit sold.

import pandas as pd
file_path = 'salesdata.csv'    # Path of the file
data = pd.read_csv(file_path)  # Read the csv file
data.head()                    # Show the 1st five items present in csv file
"""
	Region	Manager	SalesMan	Item	Units	Unit_price	Sale_amt
0	East	Martha	Alexander	Television	95	1198.0	113810.0
1	Central	Hermann	Shelli	Home Theater	50	500.0	25000.0
2	Central	Hermann	Luis	Television	36	1198.0	43128.0
3	Central	Timothy	David	Cell Phone	27	225.0	6075.0
4	West	Timothy	Stephen	Television	56	1198.0	67088.0
"""

# Create a Pivot table
# The pivot table will aggregate the units sold based on the item
pivot_table = pd.pivot_table(
    data,                     # DataFrame to be pivoted
    values='Units',           # Values to aggregate (Units sold)
    index=['Item'],           # Grouping by Item
    aggfunc='sum'             # Aggregation function: sum
)

# Display the Pivot table
print(pivot_table)

# Output:
"""
            Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395
​"""
