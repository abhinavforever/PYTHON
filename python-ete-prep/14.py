class arithmetic:
    def exp(self,b,p):
        self.base=b
        self.power=p
        prod=1
        for i in range(1,p+1):
            prod=prod*self.base
        return prod
    
a=arithmetic()
base=int(input("enter base: "))
exponent=int(input("enter exponent: "))
print(a.exp(base,exponent))
