str=input()
lst=str.split(",")
# p=1
# for i in lst:
#     p=p*i
# print(p)
for i in range(len(lst)):
    lst[i]=int(lst[i])
p=1
for i in lst:
    p=p*i
print(p)