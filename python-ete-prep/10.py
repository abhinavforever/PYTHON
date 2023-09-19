m=float(input("enter marks: "))
if m>=70 and m<=100:
    print("distinction")
elif m>=60 and m<=69:
    print("merit")
elif m>=40 and m<=59:
    print("pass")
elif m<40:
    print("fail")
else:
    print("invalid input")