#Converting a given string's lower to upper case and Vise-versa
c = input()
i = 0
j = [] #Declaring empty List
for i in range(len(c)): #For Acessing elements in string. 
    if c[i]==c[i].lower(): #For finding the Lower-case or Upper-case elements
     j.append(c[i].upper()) #Adding the new chhanged Upper-case element to j
    else :
        j.append(c[i].lower()) #Adding the new changed Lower-case elements to j
f = ''.join([str(elem) for elem in j])  #converting list to String
print(f)
#sample input : Ashish
#sample output : aSHISH
