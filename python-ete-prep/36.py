# 36. a) Assume the given instructions below to write the program
# i.Take the input values a, b from the user.
# ii. Define the function add().
# iii. It takes two arguments a and b.
# iv. Add a and b and return the result.
# v. Call this function by passing the argument values a and b and print the result.
#  b) Assume the given instructions and write the program to undertand Key arguments
# • Define a function simplecalc()
# • Takes two parameters a and b simplecalc(a, b)
# • Inside the function do all the operations +, -, * on a and b.
# • Print the result of all the operations
# • set values a = 3 and b = 4.
# • Call the method by passing two values as keyword argument one in the regular order
# and one in the reverse order.

# a)
a=int(input("a: "))
b=int(input("b: "))

def add(a,b):
    return a+b
print(add(a,b))

# b)
def simplecalc(a=3,b=4):
    print("+:",a+b)
    print("-:",a-b)
    print("*:",a*b)
    print("/:",a/b)

simplecalc(a=a,b=b)
simplecalc(b=b,a=a)
