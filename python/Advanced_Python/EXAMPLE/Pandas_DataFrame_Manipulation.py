import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [45, 85, 60]}
df = pd.DataFrame(data)

filtered_df = df[df['Score'] > 50]
print(filtered_df)
