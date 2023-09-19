def calculatearea(side1=None,side2=None):
    if side1==None and side2==None:
        print("invalid input")
    elif side1!=None and side2==None:
        print(side1**2)
    elif side1!=None and side2!=None:
        print(side1*side2)
def calculatediameter(radius):
    print(radius*2)
