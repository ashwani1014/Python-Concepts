class GS:
    
    def __init__(self,age):
        self.age=age
        
    @property    
    def age(self):
        return self._age+2   
    
    @age.setter
    def age(self, age):
        
        if 1 <= age <= 5:
            
            self._age = age  # ← Setter updates value
        else:
            raise ValueError("Age must be between 1 and 5")


tea = GS(1)

print(tea.age)      # ← Getter called automatically

 