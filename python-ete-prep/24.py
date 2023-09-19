class Car:
    def set_brandname(self,brand):
        self.brandname=brand
    def get_brandname(self):
        print(self.brandname)
    
class Accord(Car):
    def set_model(self,model):
        self.model=model
    def get_model(self):
        print(self.model)

a=Accord()
a.brandname=input("enter brandname: ")
a.get_brandname()

a.set_brandname(input("enter brandname again: "))
a.get_brandname()

a.set_model(input("enter model name: "))
print(a.model)
print(a.get_model())