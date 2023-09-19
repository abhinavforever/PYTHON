def isPerfect(n1):
    list = []
    for i in range(1, n1):
        if n1 % i == 0:
            list.append(i)
    s = 0
    for i in list:
        s = s+i
    if (s == n1):
        print("is perfect")
    else:
        print("not perfect")


n = int(input())
a = isPerfect(n)
