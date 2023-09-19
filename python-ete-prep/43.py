# Write a Python program to create a lambda function that adds 15 to a given number
# passed in as an argument, also create a lambda function that multiplies argument x with
# argument y and prints the result.

n=int(input("enter number: "))
m=int(input("enter another number: "))
print((lambda x:x+15)(n))
(lambda x,y:print(x*y))(n,m)