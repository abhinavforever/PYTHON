# 22)c)Write a simple program to convert given number into string, char and hexadecimal
# and complex number.
from ast import literal_eval
n=int(input("enter no.: "))
n=str(n)
print(n,type(n))
n=int(n)
n=hex(n)
print(n,type(n))
n=literal_eval(n)#to convert from hex to integer 
print(n)
n=oct(n)
print(n,type(n))

n=literal_eval(n)
n=complex(n)
print(n)