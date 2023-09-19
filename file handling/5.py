# 5. Write a Python program to read a file line by line and store it into a list.

f=open('fi.txt','r')
l=[]
for x in f:
    l.append(x)
print(l)

new_l=[]
for line in l:
    linee=line.replace('\n','')
    new_l.append(linee)
print(new_l)
        

