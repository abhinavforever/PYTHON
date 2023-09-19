# import numpy as np
# l="8 27 39 589 23 23 34 589 12 45 939 32 27 12 78 23 349 48 21 32".split(" ")
# l=[int(i) for i in l]
# a = list({589, 39, 27})
# arr=np.array(l)
# arr=arr.reshape(4,5)
# print(arr)
# d=dict()
# i=1
# count=0
# for row in arr:
#     count=0
#     for ele in row:
#         if ele in a:
#             count+=1
#             d[i]=count
#     if count==0:
#         d[i]=count
#     i+=1
#     count=0

# for k,v in d.items():
#     print(k,d[k])

# n=int(input())
# s=str(n)
# l=list(s)
# li=l[::-1]
# if l==li:
#     print("palindrome")


# n=int(input("enter no: "))
# k=n
# n=str(n)
# le=len(n)
# l=list(n)
# l=[int(i) for i in l]
# # n=int(n)
# s=0
# for i in l:
#     s+=i**le
# if s==k:
#     print("armstrong")
# else:
#     print("not armstrong")

# ch=input()
# v=['a','e','i','o','u']
# ch=ch.lower()
# if ch.isalpha():
#     if ch in v:
#         print("letter and vowel")
#     else:
#         print("letter and consonant")
# else:
#     print("not letter")


# n=int(input("enter no. of rows: "))
# number=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(number,end=' ')
#         number+=1
#     print()

# footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1],reverse=False)
# print(sorted_footballers_by_goals)
# print(sorted(footballers_goals.items()))

# # [('Cruyff', 104), ('Eusebio', 120), ('Messi', 125), ('Ronaldo', 132), ('Pele', 150)]

# print("\nthe\ntea")

# import packages
# import matplotlib.pyplot as plt
# import numpy as np

# # return values between 0 and 10, with a space of 0.1
# x = np.arange(0, 10, 0.1)

# # generate the value of the cos function for given x values 
# y = np.sin(x)

# # plot graph of the sine function
# plt.plot(y, color='blue')

# plt.xlim(0, 50)
# plt.ylim(0, 2)
# # display plot
# plt.show()

# r=(lambda x:x+5)(4)
# print(r)

# Importing Pandas library

# import pandas as pd

# # Creating two lists
# author = ['Jitender', 'Purnima',
# 		'Arpit', 'Jyoti']
# article = [210, 211, 114, 178]

# # Creating two Series by passing lists
# auth_series = pd.Series(author)
# article_series = pd.Series(article)

# # Creating a dictionary by passing Series objects as values
# frame = {'Author': auth_series,
# 		'Article': article_series}

# # Creating DataFrame by passing Dictionary
# result = pd.DataFrame(frame)
# re=result.to_numpy()
# # Printing elements of Dataframe
# print(result)
# print(re)

# import pandas as pd

# author = ['Jitender', 'Purnima',
# 		'Arpit', 'Jyoti']

# auth_series = pd.Series(author)

# result = pd.DataFrame(auth_series)

# re=result.to_numpy()
# # Printing elements of Dataframe
# print(result)
# #Printing elements of Numpy array
# print(re)

import pandas as pd
data = pd.DataFrame(pd.Series([1,2,3,45]))
n=data.to_numpy()
print(data)
print(n)