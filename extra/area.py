def triangle(a,b,c):
    s=(a+b+c)/2
    area= (s*(s-a)*(s-b)*(s-c))**(1/2)
    print(area)
def rectangle():
    l=float(input("enter length="))
    b=float(input("enter breadth="))
    area=l*b
    print(area)
def square():
    s=float(input("enter side="))
    area=s**2
    print(area)
def circle():
    r=float(input("enter radius="))
    area= 3.14*(r**2)
    print(area)
