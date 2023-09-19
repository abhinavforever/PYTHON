# 8. Write a python program to find the longest words.

f=open('fi.txt','r')
l=[]
list=[]
for line in f:
    l=(line.split(' '))
    for word in l:
        if '\n' in word:
            correct_word=word.replace('\n','')
            l.remove(word)
            l.append(correct_word)
    list.extend(l)
print(list)

max=len(list[0])
for word in list:
    word=str(word)
    le=len(word)
    if le>max:
        max=le
        pos=list.index(word)
print("longest word:",list[pos])

    