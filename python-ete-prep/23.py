# 23. (a) Assume the string "This is my first String". Write a program to print the following:
# print the string, print the character f using forward indexing, and print the character S
# using negative/backward indexing.

string ="This is my first String"
print(string)
i=string.index("f")
print(string[i])

l=len(string)
i2=string.index("S")
print(string[-(l-i2)])

# (b) Test for two inputs from the user using input() function, one is string str and another
# one is integer n. Write a program to print the given string str n times. Print the result
# as shown in the example.
s=input("enter string: ")
n=int(input("enter number: "))

for i in range(n):
    print(s)
