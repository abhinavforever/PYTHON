def pascal(n):
    trow = [1]
    y = [0]
    for i in range(max(n, 0)):
        print(trow)
        trow = [l+r for l, r in zip(trow+y, y+trow)]
# i=0:
# trow=[1]
# y=[0]
# trow+y=[1,0]
# y+trow=[0,1]
# zip(trow+y,y+trow)=zip([1,0]+[0,1])=(1,0) (0,1) .The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.

# since zip is not a set or list or tuple:
# l,r in 1st item of zip is l=1,r=0 so l+r=1+0=1
# l,r in 2nd item of zip is l=0,r=1 so l+r=0+1=1

# trow=[l+r for l,r in zip(trow+y,y+trow)] = [1,1]

# similarly,
# for i=1:
# trow=[1,1]
# y=[0]
# zip(trow+y,y+trow)=zip([1,1,0],[0,1,1])=(1,0) (1,1) (0,1)

# for 1st item of zip: l+r for l,r in zip=1+0=1
# for 2nd item of zip:l+r for l,r in zip=1+1=2
# for 3rd item of zip:l+r for l,r in zip=0+1=1 

# and so on...

pascal(6)
