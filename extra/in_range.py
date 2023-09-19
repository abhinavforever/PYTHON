# Write a Python function to check whether a number falls in a given range.
rl = int(input())
ru = int(input())
n = int(input())
k = 0
for i in range(rl, ru+1, 1):
    if i == n:
        print("yes")
        k = 1
        break
if (k == 0):
    print("no")
