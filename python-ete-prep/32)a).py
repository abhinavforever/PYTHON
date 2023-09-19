# 32. a) Construct a python program to change Dictionary keys into values and values into
# keys, and print the result.

d=dict()
l1=[i for i in range(1,11)]
l2=[i for i in range(11,21)]
for i,j in zip(l1,l2):
    d[i]=j
print(d)

d2=dict()
for k,v in d.items():
    d2[v]=k
d=d2
print(d)