
# from datetime import datetime
# odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
#         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#         41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# right_this_minute = datetime.today().minute
# if right_this_minute in odds:
#     print("This minute seems a little odd.")
# else:
#     print("Not an odd minute.")

# from datetime import datetime
# import time
# import random
# odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
#         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#         41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# for i in range(5):
#     right_this_minute = datetime.today().minute
#     if right_this_minute in odds:
#         print("This minute seems a little odd.")
#     else:
#         print("Not an odd minute.")
#     wait_time = random.randint(1, 10)
#     time.sleep(wait_time)

# word = "bottles"
# for beer_num in range(99, 0, -1):
#     print(beer_num, word, "of beer on the wall.")
#     print(beer_num, word, "of beer.")
#     print("Take one down.")
#     print("Pass it around.")
#     if beer_num == 1:
#         print("No more bottles of beer on the wall.")
#     else:
#         new_num = beer_num - 1
#         if new_num == 1:
#             word = "bottle"
#         print(new_num, word, "of beer on the wall.")
#     print()

# vowels = ['a', 'e', 'i', 'o', 'u']
# word = "Milliways"
# for letter in word:
#     if letter in vowels:
#         print(letter)

# vowels = ['a', 'e', 'i', 'o', 'u']
# word = "Milliways"
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print(vowel)

# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Provide a word to search for vowels: ")
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowel in found:
#     print(vowel)

# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)
# for i in range(4):
#         plist.pop()
# plist.pop(0)
# plist.remove("'")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
# new_phrase = ''.join(plist)
# print(plist)
# print(new_phrase)

# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)
# new_phrase = ''.join(plist[1:3])
# new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
# print(plist)
# print(new_phrase)

# paranoid_android = "Marvin"
# letters = list(paranoid_android)
# for char in letters:
#     print('\t', char)

# paranoid_android = "Marvin, the Paranoid Android"
# letters = list(paranoid_android)
# for char in letters[:6]:
#     print('\t', char)
# print()
# for char in letters[-7:]:
#     print('\t'*2, char)
# print()
# for char in letters[12:20]:
#     print('\t'*3, char)
