phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
x=len(plist)
for item in range(12):
    plist.pop()
str="on tap"
slist=list(str)
plist.extend(slist)
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
    
