# 37. Which string method is used to implement the following?
# (i) To check whether the given character is a letter or a number.

s = input("enter char or string or any text: ")
# 0 means not present in the string, 1 means present in the string
l = 0
n = 0
sc = 0
sp = 0
for chr in s:
    if chr.isalpha():
        l = 1
    elif chr.isdigit():
        n = 1
    elif chr.isspace():
        sp = 1
    elif not (chr.isspace() or chr.isalpha() or chr.isdigit()):
        sc = 1
if l == 1:
    print("alphabets are present")
if n == 1:
    print("numbers are present")
if sc == 1:
    print("special characters are present")
if sp == 1:
    print("spaces are present")
# (ii) To change lower case to upper case letter.

str=input("enter string in any case: ")
print(str.upper())