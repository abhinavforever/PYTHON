# Using regular expression, write a python program to check that a string contains
# only a certain set of characters (in this case a-z, A-Z and 0-9).

import re

s=input("enter string : ")

x=re.findall("[a-zA-Z0-9]",s)
print(x)

l=s.split(" ")
li=[]
for ele in l:
    li.extend(list(ele))
print(li)
if li==x:
    print("string contains characters a-z, A-Z and 0-9 only ")
else:
    print("string contains characters apart from a-z, A-Z and 0-9 also")
    
