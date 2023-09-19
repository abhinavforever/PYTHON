import pandas as pd
df=pd.read_csv('friends.csv')
df.index=['first','second','third','fourth']

df.drop(labels=['second','third'],inplace=True)
df.drop('city',axis=1,inplace=True)
print(df)