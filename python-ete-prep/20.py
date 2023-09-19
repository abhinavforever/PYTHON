numbers = [12, 75, 150, 180, 145, 525, 50]
l=[]
for n in numbers:
    if n>500 :
        break
    if n>150:
        continue
    if n%5==0:
        l.append(n)

for ele in l:
    print(ele)