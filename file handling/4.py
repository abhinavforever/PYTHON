# Write a Python program to read last n lines of a file.

f=open('fi.txt','r')
n=3
c=0
for i in f:
    c+=1
print(c) #no. of lines in the file

