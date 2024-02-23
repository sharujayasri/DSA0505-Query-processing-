import pandas as pd
import numpy as np

# Create a DataFrame with 10 rows and 4 columns with random values
data = np.random.rand(10, 4)
columns = ['Column1', 'Column2', 'Column3', 'Column4']
df = pd.DataFrame(data, columns=columns)

# Function to set background color to black and font color to yellow
def style_black_yellow(val):
    return 'background-color: black; color: yellow'

# Apply the style to the DataFrame
styled_df = df.style.apply(lambda x: x.applymap(style_black_yellow))

# Display the styled DataFrame
styled_df.to_excel('output_styled.xlsx', engine='openpyxl', index=False)  # Save to an Excel file for better visibility
styled_df
