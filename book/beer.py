word="bottles"
for beer_num in range(10,0,-1):
    if(beer_num==1):
        word="bottle"
    print(beer_num,word,"of beer on the wall.")
    print(beer_num,word,"of beer.")
    print("Take one down.")
    print("Pass it around.")
    new_num=beer_num-1
    if(new_num==0):
        print("No more bottles of beer on the wall.")
    elif(new_num==1):
        word="bottle"
        print(new_num,word,"of beer on the wall.")
    else:
        print(new_num,word,"of beer on the wall.")
    print()
#Imagine you have few lines of code above this 
input() 
