# Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def multiply(list1, len1):
    p = 1
    for i in range(len1):
        p = p*list1[i]
    print("product:", p)


list = []
len = int(input("enter len of list:"))
for i in range(len):
    list.append(int(input(f"enter number {i}:")))
multiply(list, len)
