# import pandas as pd
# import numpy as np
# # d={'one':10,'two':20,"three":30}
# # s=pd.Series(data=d,name='my')
# # d=np.array([1,2,3,4],dtype=int)
# d=np.random.randint(10)
# i=['one','two','three','four']
# s=pd.Series(d,index=i)
# print(s)

# import pandas as pd
# import numpy as np

# a=np.array([['a','b','c'],['d','e','f']])
# print(a)
# b=np.array([['d','e','f'],['a','b','c']])
# print(b)

# c=np.char.add(a,b)
# print(c)

# e="hi bye"
# f=np.char.multiply(e,3)
# print(f)

# g=np.char.center(e,20,"$")
# print(g)


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# x=['one','two','three']
# y=[23,4,5]
# a=plt.bar(x,y,width=0.8)
# plt.ylim(0,30)
# plt.xlabel("x-axis yo")
# plt.ylabel("y-axis yo")
# plt.title("my graph yo")
# plt.show()

# l=['red','green','blue']
# b=plt.pie(y,colors=l,startangle=90)
# plt.show()


# from matplotlib import pyplot as plt
# import numpy as np
# fig,ax = plt.subplots(1,1)
# a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
# ax.hist(a, bins = [0,25,50,75,100])
# ax.set_title("histogram of result")
# ax.set_xticks([0,25,50,75,100])
# ax.set_xlabel('marks')
# ax.set_ylabel('no. of students')
# plt.show()

# import numpy as np
# import pandas as pd

# a=np.array([[1,2,3],[5,5,6]],ndmin=2)
# b=np.array([4,5,6])
# df=pd.DataFrame(a)
# # print(a+b)

# print(np.power(a,b))
# print(np.mod(a,b))
# print(np.max(a))
# print(np.min(a))

# print(np.mean(a))
# print(np.std(a))
# print(np.var(a))
# print(np.median(a))
# print(np.cumsum(a))
# print(np.cumproduct(b))
# print(np.prod(b))


# a=np.arange(1,19,2,dtype=float)
# print(a)

# s=pd.Series([23,45,56,71])
# t=pd.Series([1,2,4,5])
# di={'first':s,'second':t}
# df=pd.DataFrame(data=di)
# print(df)

# #add row 
# df.loc[len(df.index)]={'first':234,'second':45.6}
# print(df)

# #delete row
# df.drop(1,inplace=True)
# print(df)

# #add column
# df['third']=pd.Series([2,3,4,5,0])
# print(df)

# #remove column
# df.drop('third',axis=1,inplace=True)
# print(df)

# #slice row 
# print(df[0:3])

# print(df.head(2))
# print(df.tail(2))

# di={'first':pd.Series([1,2,3]),'second':pd.Series([4,5,6])}
# df=pd.DataFrame(di)
# print(df)

# print(df.transpose())

# print(df.info())
# print(df.describe())

# print(df.min())