import pandas as pd

# Display the dimensions (shape) of the dataset
dimensions = world_alcohol_consumption.shape
print(f"Dimensions of the dataset: {dimensions}")

# Extract and display the column names
column_names = world_alcohol_consumption.columns.tolist()
print(f"Column names of the dataset: {column_names}")
