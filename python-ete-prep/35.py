# 35. Assume the given below instructions to implements the method overriding method:
# • Define class Animal
# • Use constructor to set the name with a default value = "This Animal"
# • Define a method eat with a parameter food with a default value = "Grass"
# • Inside the method print (self.name, " eats", food)
# • Define a class Mammal, inherit from Animal
# • Inside the class, override eat method to print(self.name, " does not eat. It only drinks")
# • Define class WingedAnimal, inherit from Animal
# • Override eat method to print(self.name," eats anything and everything")
# • Define a class called Bat, inherit from WingedAnimal, Mammal
# • Define method smell, which prints "This Animal Stinks"
# • Define a class called FruitBat, inherit from Mammal, WingedAnimal (Notice the Order)
# • rabbit1 = Animal("Rabbit")
# • print("Rabbit1 is an instance of Animal")
# • rabbit1.eat() # Animal's eat method without food parameter
# • rabbit1.eat("Peanuts") # Animal's eat method with food parameter
# • print("Cow1 is an instance of Mammal")
# • cow1 = Mammal("Cow")
# • cow1.eat() # Mammal's eat method
# • print("Vulture1 is an instance of WingedAnimal")
# • vulture1 = WingedAnimal("Vulture")
# • vulture1.eat() # WingedAnimal's eat method
# • print("Bat1 is an instance of Bat")
# • bat1 = Bat("Bat")
# • bat1.eat() # WingedAnimal's eat method
# • print("fbat is an instance of FruitBat")
# • fbat = FruitBat("Fruitbat")
# • fbat.eat() # Mammal's eat method.

class Animal:
    def __init__(self,name) -> None:
        self.name="This Animal"
    
    def eat(self,food="Grass"):
        print(self.name,"eats",food)
    
class Mammal(Animal):
    def eat(self):
        # super().eat()
        print(self.name,"does not eat. It only drinks")

class WingedAnimal(Animal):
    def eat(self):
        print(self.name,"eats anything and everything")

class Bat(WingedAnimal,Mammal):
    def smell(self):
        print("This Animal Stinks")

class FruitBat(Mammal,WingedAnimal):
    pass

rabbit1=Animal("Rabbit")
print("Rabbit1 is an instance of Animal")
rabbit1.eat()
rabbit1.eat("Peanuts")

print("Cow1 is an instance of Mammal")
cow1 = Mammal("Cow")
cow1.eat()

print("Vulture1 is an instance of WingedAnimal")
vulture1 = WingedAnimal("Vulture")
vulture1.eat()

print("Bat1 is an instance of Bat")
bat1 = Bat("Bat")
bat1.eat()

print("fbat is an instance of FruitBat")
fbat = FruitBat("Fruitbat")
fbat.eat()