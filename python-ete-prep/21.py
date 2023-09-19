#21)b)
import numpy as np
l="8 27 39 589 23 23 34 589 12 45 939 32 27 12 78 23 349 48 21 32".split(" ")
l=[int(i) for i in l]
a=np.array(l)
a=a.reshape(4,5)
print(a)

arr = list({589, 39, 27})
print("array:",arr)
d={}
i=1
count=0
for row in a:
    for ele in row:
        if ele in arr:
            count+=1
            d[i]=count
    if count==0:
        d[i]=0
    i+=1
    count=0

# print(d)

for i,j in d.items():
    print("row",i,"has",j,"items of array")