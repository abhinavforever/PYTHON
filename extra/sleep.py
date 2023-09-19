# Write a Python program that invoke a given function after specific milliseconds.
from time import sleep


def max(list1, ms):
    sleep(ms/1000)
    max = list1[0]
    for i in range(1, 3):
        if list1[i] > max:
            max = list1[i]
    print(max)
    sleep(ms/1000)

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
max(list, 5000)
