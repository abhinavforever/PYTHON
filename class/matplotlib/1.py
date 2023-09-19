import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y1=[s**2 for s in x]
y2=[s**3 for s in x]
y3=[s**0.5 for s in x]
y4=[s+10 for s in x]

plt.plot(x,y1,"blue",label="square fn")
plt.plot(x,y2,'green',label="cubic fn")
plt.plot(x,y3,'--r',label="square root function")
plt.plot(x,y4,'black',label='linear function')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Mathematical Functions")
plt.legend()
plt.show()
