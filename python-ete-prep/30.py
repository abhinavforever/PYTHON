# 30. a) Assume three strings to compare. Using else-if compare then and print the longest
# string.
s1=input()
s2=input()
s3=input()
print("longest string is : ")

if len(s1)>len(s2):
    if len(s1)>len(s3):
        print(s1)
    elif len(s1)<len(s3):
        print(s3)
    else:
        print(s1)
        print(s3)
        #since both have equal length
elif len(s1)<len(s2):
    if len(s2)> len(s3):
        print(s2)
    elif len(s2)<len(s3):
        print(s3)
    else:
        print(s2)
        print(s3)
else:
    print(s1)
    print(s2)

print("\n")
# (b) Assume the string str = “Bangalore”, Iterate it using for loop, and print characters
# vertically.
str = "Bangalore"
for char in str:
    print(char)
