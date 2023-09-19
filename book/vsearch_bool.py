def search4vowels(word):
 """Return a boolean based on any vowels found."""
 vowels = set('aeiou')
 found = vowels.intersection(set(word))
 return bool(found)
''' is found is a non-empty set i.e. a non-empty data structure then True is
returned otherwise if found is an empty data structure then False is returned'''
