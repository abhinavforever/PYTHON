import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("D:\python\class\matplotlib\iris.csv")
print(data)
df2=data.iloc[:,0:4]
print(df2)
sb.heatmap(df2.corr())
plt.show()