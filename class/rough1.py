import numpy as np
a=np.arange(0,101,5)
index=0
a_5=[]
a_10=[]
print(a)
for i in a:
    if i%5==0 and i%10!=0:
        a_5.append(i)
    else:
        a_10.append(i)
a_5=np.array(a_5)
a_10=np.array(a_10)
print(a_5)
print(a_10)
a=np.delete(a,index)
a.shape=(5,4)
print(a)
