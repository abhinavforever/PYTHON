import math as m
a=34
b=4
print(a/b) #actual value
print(a//b) #quotient
print(a%b) #remainder
print(a<<b) #left shift operator: N<<2 then N=N*(2^2)
print(a>>b) #right shift operator : N>>2 then N=N/(2^2) and N is a ceiled whole number only
print(35>>2) #35/4 = 8.75 so we get ceil(8.75)=8
print(m.ceil(4.1),m.floor(4.6))
print(abs(-9.1))
str1="hi"*3
print(str1)
print(5|7)#bitwise or does 'or' of binary 5 and binary 7
print(5&7)#bitwise and does 'and' of binary 5 and bnary 7
print(5^7)#bitwise xor does 'xor' of binary 5 and binary 7
print(True or False)
print(True and False)
print("{0:.3f}".format(m.pi))
