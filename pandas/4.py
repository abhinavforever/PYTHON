import pandas as pd

s1=pd.Series(['a','b','c'],index=[1,2,3])
s2=pd.Series(["cd","ef","gh"],index=[4,5,6])
s3=pd.Series(["m","n","o"],index=[1,2,3])

d={"col1":s1,"col2":s2,"col3":s3}

df=pd.DataFrame(d)
print(df)
print(df.T)
print(df.head())
print(df.tail())

print(df.info())
print(df.describe())