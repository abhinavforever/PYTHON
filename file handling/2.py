# Write a Python program to read first n lines of a file.

f=open('fi.txt')
n=3
for x in range(n):
    print(f.readline(),end='')