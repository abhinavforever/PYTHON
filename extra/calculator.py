def add(n):
    print("the number of numbers to be added=",n)
    sum=0
    for i in range(0,n):
        num=float(input("enter number:"))
        sum=sum+num
    print("sum=",sum)
def prod(n):
    print("the number of numbers to be multiplied=",n)
    prod=1
    for i in range(0,n):
        num=float(input("enter number:"))
        prod=prod*num
    print("product=",prod)
def div(a,b):
    n=int(input("for float division press 1 else press 2:"))
    if(n==1):
        return a/b
    else:
        return a//b
def sub(a,b):
    return a-b
def power(a,b):
    return a**b
def si(p,r,t):
    return ((p*r*t)/100)
def ci(p,r,t):
    return (p*pow((1+r/100),t))
