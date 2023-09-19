# 33. a. Identify different methods available in python 
# dictionaries to add, remove, or change elements within a 
# dictionary, including their syntax, parameters, and output.

d=dict()
l1=[i for i in range(1,11)]
l2=[i for i in range(11,21)]
for i,j in zip(l1,l2):
    d[i]=j
print(d)

#add element
d[100]=200
print(d)

#remove element
del d[100]
print(d)

#change element
d[7]=200
print(d)

# b)Make Use of the "pop" method present in python dictionaries
d.pop(5)
print(d)