import pandas as pd

data = {
    "Name": ["Aisha", "Luis", "Chen", "Amara"],
    "Age": [24, 27, 22, 32],
    "City": ["New York", "San Francisco", "Beijing", "Nairobi"]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

print("\nSummary Statistics:")
print(df.describe())