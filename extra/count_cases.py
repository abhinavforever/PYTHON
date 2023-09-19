# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
str = input()
l = 0
u = 0
n = 0
j = 1
for i in str:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1

print("lowercase=", l)
print(f"uppercase={u}")
