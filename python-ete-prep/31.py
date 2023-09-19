# 31. a) Construct a tuple with the user-given elements and concatenate both the tuples and
# print the result.

a=input()
b=input()

t1=tuple(a)
t2=tuple(b)

print(t1+t2)

#  (b) Construct a tuple with the user-given inputs. Write a program using membership
# operators to check whether the given element is present in the tuple or not. Print the result.

a=input()
l=a.split(" ")
t1=tuple(l)
ele=input()
if ele in t1: #if word in tuple
    print("yes")
else:
    print("no")

#  (c) Apply a python program to add an element to a tuple based on the user-given value
# in a specific index, and print the result as shown in the example. If the index is not in the
# range print the error message as shown in the example.

s=input("enter string to make tuple from: ")
t=tuple(s)

i=int(input("index : "))
ele=input()
l=len(t)
if i>l or i<0:
    print("error")
else:
    l=list(t)
    l.insert(i,ele)
    t=tuple(l)
print(t)