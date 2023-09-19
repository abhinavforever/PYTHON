# Write a Python function that takes a number as a parameter and check the number is prime or not
def prime(a):
    k = 0
    for i in range(1, a+1):
        if (a % i == 0):
            k += 1
        else:
            continue
    if k > 2 or a==1:
        print("not prime")
    elif k == 2 :
        print("prime")


a = int(input())
prime(a)
