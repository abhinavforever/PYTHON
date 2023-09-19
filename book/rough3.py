import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

len_l = len(letters)
len_s = len(symbols)
len_n = len(numbers)


def funl(len_l, nr_letters, countl):
    if countl < nr_letters:
        l = random.randint(1, nr_letters-countl)
        for i in range(l):
            c = random.randint(0, len_l-1)
            print(letters[c], end='')
        return countl+l


def funs(len_s, nr_symbols, counts):
    if counts < nr_symbols:
        # s denotes the random number of times for loop iterates for a particular call
        s = random.randint(0, nr_symbols-counts)
        # for loop prints the random symbols for s times
        for i in range(s):
            c = random.randint(0, len_s-1)
            print(symbols[c], end='')
        return counts+s


def funn(len_n, nr_numbers, countn):
    if countn < nr_numbers:
        n = random.randint(0, nr_numbers-countn)
        for i in range(n):
            c = random.randint(0, len_n-1)
            print(numbers[c], end='')
        return countn+n


t = nr_letters+nr_numbers+nr_symbols
countl = 0
countn = 0
counts = 0
k = 0
for i in range(t):
    if (k != t):
        c = random.randint(1, 3)
        if (c == 1 and countl != nr_letters):
            countl = funl(len_l, nr_letters, countl)
            k += countl
        elif (c == 2 and countl != nr_symbols):
            counts = funs(len_s, nr_symbols, counts)
            k += counts
        elif (c == 3 and counts != nr_numbers):
            countn = funn(len_n, nr_numbers, countn)
            k += countn
