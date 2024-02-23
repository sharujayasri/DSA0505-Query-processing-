import pandas as pd

# Assuming your data is stored in a DataFrame named sales_data
# Example data creation (replace this with your actual data)
data = {
    'Item': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sale': [100, 150, 200, 120, 180, 90],
}

sales_data = pd.DataFrame(data)

# Create a Pivot table to find maximum and minimum sale values
pivot_table = pd.pivot_table(sales_data, values='Sale', index='Item', aggfunc={'Sale': ['max', 'min']})

# Rename columns for clarity
pivot_table.columns = ['Max_Sale', 'Min_Sale']

# Display the result
print("Pivot Table with Max and Min Sale Values:")
print(pivot_table)
