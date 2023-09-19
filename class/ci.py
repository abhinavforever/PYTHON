p=float(input("principal:"))
r=float(input("rate:"))
t=float(input("time:"))
ci=p*((1+r/100)**(t/12))
print(ci)
a=p+ci
print(a)
