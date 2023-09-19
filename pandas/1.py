import pandas as pd
df=pd.read_csv('friends.csv')
df.index=['first','second','third','fourth']
s=pd.Series(df['name'])
print(s)

s1=s.copy(deep=False)
s1['first']="hari puttar"
print(s1)
print(s)

s2=s.copy(deep=True)
s2['first']="balle balle"
print(s2)
print(s)