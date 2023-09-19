import pandas as pd
df=pd.DataFrame()
print(df)

df.index=[1,2,3]
df["name"]=['a','b','c']
df['age']=[11,22,33]
print(df)

df.iloc[0,0]='ete'
df.loc[1,'age']=123
print(df)