# Write a Python program to append text to a file and display the text.

f=open('fi.txt','a')

f.write("\nnew text")
f.close()

f=open('fi.txt')
print(f.read())
f.close()