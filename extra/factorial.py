# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def fact(n):
    p = 1
    for i in range(1,n+1):
        p = p*i
    return p

n = int(input())
if n >= 0:
    print(fact(n))
else:
    print("negative number")
