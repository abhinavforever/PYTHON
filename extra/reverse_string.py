# Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

string = input("enter a string:")
l = len(string)
s=string[-1:-(l+1):-1]
print(s)