n=int(input("enter the number of terms in the fibonacci series to be printed:\t"))
a=1
b=1
print(a,b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
    
