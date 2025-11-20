import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/sales.csv")

# Drop missing values
df.dropna(inplace=True)

# Print cleaned data
print(df)
