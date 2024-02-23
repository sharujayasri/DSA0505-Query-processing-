import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'Age': [25, 22, 23, 24, 28, 22],
        'School Code': ['S001', 'S002', 'S001', 'S002', 'S003', 'S001'],
        'Class': ['A', 'B', 'A', 'B', 'C', 'A']}

df = pd.DataFrame(data)

# Group the DataFrame by 'School Code' and 'Class'
grouped_df = df.groupby(['School Code', 'Class'])

# Display the groups and their contents
for name, group in grouped_df:
    print(f"Group Name: {name}")
    print(group)
    print("\n")
