n=int(input("enter number: "))

s=str(abs(n))
l=list(s)
l.reverse()
s2=''.join(l)
if s==s2:
    print("palindrome")
else:
    print("not palindrome")
