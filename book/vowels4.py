a=0
e=0
i=0
o=0
u=0
word=input("enter your word:\t")
found={}

for letter in word:
    if letter=='a' :
        a+=1
    elif letter=='e' :
        e+=1
    elif letter=='i' :
        i+=1
    elif letter=='o' :
        o+=1
    elif letter=='u' :
        u+=1
found['a']=a
found['e']=e
found['i']=i
found['o']=o
found['u']=u
for kv in found:
    print(kv , "was found ", found[kv] , "time(s)")
