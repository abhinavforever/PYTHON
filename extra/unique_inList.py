# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(list1, len1):
    list2 = []
    for i in list1:
        if (i not in list2):
            list2.append(i)
        else:
            continue
    print(list2)
list = []
len = int(input("enter len of list:"))
for i in range(len):
    list.append(input())
unique(list,len)