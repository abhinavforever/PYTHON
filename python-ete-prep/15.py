s=input()
print(len(s))
count=0
for i in s:
    if i.isspace()==False:
        count+=1
print("no. of characters: ",count)
l=list(s)
l[0]=l[0].upper()
s=''.join(l)
print(s)

print(s.capitalize())
print(s.title())