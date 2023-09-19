import math as m
a=input("enter your first name :")
b=input("enter your last name:")
str1="hello ms.{}.Do you mind if I call you {}?".format(b,a)
print(str1)
str2="hello ms.{1}.Do you mind if I call you {0}?".format(a,b)
print(str2)
str3= f"hello ms.{b}.Do you mind if I call you {a}?"
print(str3)
str4="my name is {fname}.I am {age} years old.".format(fname="abhinav",age = 21)
print(str4)
#---#
print("hi\nthis is a new line")
print(r"hi\nthis is a new line")
#---#
def MyFunction():
    print("this is my function")
MyFunction()
#---#
print("floating point pi={0:.3f},with {1:d} digit precision".format(m.pi,3))
