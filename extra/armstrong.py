n=int(input("enter the number to be checked for Armstrong number:"))
temp=n
sum=0
while temp!=0:
    q=temp//10
    r=temp%10
    sum=sum+(r**3)
    temp=q
if n==sum:
    print("Armstrong")
else:
    print("Not Armstrong")
