# 1) Write a python program to create a DataFrame from an existing series, add and delete row and columns; slice row; and print head and tail to a Pandas DataFrame.
import pandas as pd

s=pd.Series([1,2,3,4])
t=pd.Series([11,22,33,44])

di={"first":s,"second":t}

df=pd.DataFrame(data=di)
print(df)

df.loc[len(df.index)]={"first":5,"second":55}
print(df)

df.drop(1,inplace=True)
print(df)

df["third"]=pd.Series([4,5,6,8,9])
print(df)

df.drop("third",axis=1,inplace=True)
print(df)

print(df[1:3])
print(df.head(2))
print(df.tail(2))