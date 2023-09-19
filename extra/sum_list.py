# Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum_list(list1, len1):
    s = 0
    for i in range(len1):
        s = s+list1[i]
    print("sum of numbers in list:", s)


list = []
len = int(input("enter len of list:"))
for i in range(len):
    list.append(int(input(f"enter number {i}:")))
sum_list(list,len)
