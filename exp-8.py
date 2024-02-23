import pandas as pd

# Assuming your data is in a DataFrame named sales_data
# Example data creation (replace this with your actual data)
data = {
    'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-03'],
    'Item': ['A', 'B', 'A', 'B', 'A'],
    'Unit_Sold': [10, 15, 20, 12, 18],
    'Sale_Value': [100, 150, 200, 120, 180],
}

sales_data = pd.DataFrame(data)

# Convert 'Date' column to datetime format
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Create a pivot table for item-wise unit sold
pivot_table_unit_sold = pd.pivot_table(sales_data, values='Unit_Sold', index='Item', aggfunc='sum')

# Create a pivot table for maximum and minimum sale values
pivot_table_max_min_sale = pd.pivot_table(sales_data, values='Sale_Value', index='Item', aggfunc={'Sale_Value': ['max', 'min']})

# Display the results
print("Item-wise Unit Sold:")
print(pivot_table_unit_sold)
print("\nMaximum and Minimum Sale Values:")
print(pivot_table_max_min_sale)
