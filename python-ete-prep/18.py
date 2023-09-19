from Module_Imp3 import *
side1=int(input("enter side1: "))
side2=int(input("enter side2(otherwise type 0): "))
if side2==0:
    calculatearea(side1)
elif side2!=0:
    calculatearea(side1,side2)
calculatediameter(3)