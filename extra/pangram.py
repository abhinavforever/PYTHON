# Write a Python function to check whether a string is a pangram or not. Go to the editor
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def pangram(str):
    k = 0
    list = []
    for i in str:
        if i in a:
            if i not in list:
                list.append(i)
    if (len(list) == len(a)):
        print("pangram")
    else:
        print('not pangram')


str = input()
pangram(str)
