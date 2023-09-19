# Write a Python program to access a function inside a function.
def max(list1):
    max = list1[0]
    for i in range(1, 3):
        if list1[i] > max:
            max = list1[i]
    print(max)

    def min(list1):
        min = list1[0]
        for i in range(1, 3):
            if list[i] < min:
                min = list[i]
        print(min)
    min(list1)


list = []
for i in range(3):
    list.append(int(input(f"enter number {i}:")))
max(list)
