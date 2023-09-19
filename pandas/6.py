import pandas as pd
df=pd.read_csv('friends.csv')
print(df.sort_index(ascending=False))
print(df.sort_index(ascending=True))
print(df.sort_values(by=["marks"]))