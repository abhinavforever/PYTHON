r=int(input("ram's age: "))
s=int(input("sam's age: "))
k=int(input("khan's age: "))
l=list((r,s,k))
len=len(l)
max=l[0]
min=l[len-1]
for i in l:
    if i>=max:
        max=i
    if i<=min:
        min=i
print("youngest:",min,"eldest:",max)