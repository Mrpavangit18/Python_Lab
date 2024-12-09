# Task 1: Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.

import pandas as pd             
file_path = 'salesdata.csv'     # Path of the file 
data = pd.read_csv(file_path)   # Read the csv file 
data.head()                     # Show the 1st five items present in csv file
"""
	Region	Manager	SalesMan	Item	Units	Unit_price	Sale_amt
0	East	Martha	Alexander	Television	95	1198.0	113810.0
1	Central	Hermann	Shelli	Home Theater	50	500.0	25000.0
2	Central	Hermann	Luis	Television	36	1198.0	43128.0
3	Central	Timothy	David	Cell Phone	27	225.0	6075.0
4	West	Timothy	Stephen	Television	56	1198.0	67088.0
"""

# Create a Pivot table
# The pivot table will aggregate the sale amounts based on Region, Manager, and SalesMan
pivot_table = pd.pivot_table(
    data,                          # DataFrame to be pivoted
    values='Sale_amt',             # Values to aggregate
    index=['Region', 'Manager', 'SalesMan'],  # Levels to index by
    aggfunc='sum'                  # Aggregation function: sum
)

# Display the Pivot table
print(pivot_table)

# Output:
"""
                          Sale_amt
Region  Manager SalesMan           
Central Douglas John       124016.0
        Hermann Luis       206373.0
                Shelli      33698.0
                Sigal      125037.5
        Marth   Steven      14000.0
        Martha  Steven     185690.0
        Timothy David      140955.0
East    Douglas Karen       48204.0
        Martha  Alexander  236703.0
                Diana       36100.0
West    Douglas Michael     66836.0
        Timothy Stephen     88063.0
# Create a Pivot table
"""
