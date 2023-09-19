# Write a Python function to find the Max of three numbers.

def max(list1):
    max = list1[0]
    for i in range(1, 3):
        if list1[i] > max:
            max = list1[i]
    print(max)


list = []
for i in range(3):
    list.append(int(input(f"enter number {i}:")))
max(list)
