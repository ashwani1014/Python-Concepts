class Self:
    def __init__(self,price):
         self.price=price
    
    def describe(self):
        return f"yes If u want to buy this stick then u have to pay {self.price} ruppees"
    
c=Self(10)
print(c.describe())    



#If We want to use the variable of the class with their method then we use self 

# for method


class Student:

    def show(self):
        print("Show Method")

    def greet(self):
        print("Greeting...")
        self.show()   # current object ka method call

s1 = Student()
s1.greet()