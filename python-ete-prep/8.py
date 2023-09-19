class Person:
    def setname(self,name):
        self.name=name
    def getname(self):
        print(self.name)
class Student(Person):
    def setage(self,age):
        self.age=age
    def getage(self):
        print(self.age)
s1=Student()
n=input("enter name:")
a=int(input("enter age:"))
s1.setname(n)
s1.setage(a)
s1.getname()
s1.getage()