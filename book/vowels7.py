word = input("Provide a word to search for vowels: ")
vset=set('aeiou')
i=vset.intersection(set(word))
for letter in sorted(i):
    print(letter)

