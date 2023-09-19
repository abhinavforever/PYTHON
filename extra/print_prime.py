print('enter upper limit and lower limit:')
a=int(input("lower limit:"))
b=int(input("upper limit:"))
k=0
for i in range(a,b+1):
    for j in range(1,i+1):
        if i%j == 0:
            k+=1
    if k==2:
        print(i)
    else:
        continue