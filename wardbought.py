# Import required libraries
import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with the actual file path)
df = pd.read_csv('./data/stats1.csv')
df2 = pd.read_csv('./data/stats2.csv')

# Display unique values from the 'wardbought' column
unique_values_1 = df['wardsbought'].unique()
unique_values_2 = df2['wardsbought'].unique()
print("Unique values in 'wardbought' column from stat1:", unique_values_1)
print("Unique values in 'wardbought' column from stat2:", unique_values_2)