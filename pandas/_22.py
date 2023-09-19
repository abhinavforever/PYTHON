# 2)Write a python program to create a DataFrame and perform row and column selection, addition and deletion operations in a sample supermarket data.

import pandas as pd

# Create a data frame
df = pd.DataFrame({
    'Item': ['Apple', 'Orange', 'Banana', 'Mango', 'Pineapple'],
    'Price': [1.5, 1.0, 0.75, 2.0, 2.5],
    'Quantity': [5, 10, 15, 20, 25]
})

# Select the row with the index 2
row_2 = df.iloc[2]
row_two=df.loc[2]
print(row_2)
print(row_two)
# Select the column named 'Price'
column_price = df['Price']
print(column_price)
# Add a new row with the values 'Watermelon', 3.0, and 10
df.loc[4] = ['Watermelon', 3.0, 10]

# Delete the row with the index 2
df = df.drop(2)

# Delete the column named 'Quantity'
df = df.drop('Quantity', axis=1)

# Print the data frame
print(df)