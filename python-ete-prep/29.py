# 29. (a) Show a python program to print multiplication table of a given number.


n=int(input("enter number : "))
li=int(input("enter limit : "))

for i in range(1,li+1):
    print(n,"*",i,"=",n*i)


# (b) Explain the syntax to read a string from the right-hand side. Consider str = “Python is
# a wonderful Language”. Reverse and print the str from the right-hand side.

str ="Python is a wonderful Language"
l=str.split(" ")

for ele in l:
    ind=l.index(ele)
    ele_l=list(ele)
    ele_l.reverse()
    ele=''.join(ele_l)
    l[ind]=ele
    
l.reverse()
print(' '.join(l))