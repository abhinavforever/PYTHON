# (b)Choose an integer sequence from the user. Write a program to print a dictionary from the
#  given sequence. Consider the element in the sequence as a key, and the number of times
#  the element occurs in the sequence as a value. Print the result.

l=[]
for i in range(1,6):
    for j in range(1,6):
        if i%j==0:
            l.append(j)
print(l)

# just created a random list with the factors of numbers 1-5 that lie in the range of 1-5 only 

d=dict()
for ele in l:
    d[ele]=l.count(ele)
print(d)
