import animals.mammal as ml

class Dog(ml.Mammal):
    def __init__(self,name,age,fur_color,breed):
        super().__init__(name,age,fur_color)
        self.breed = breed
        
    def speak(self):
        
        return f"{self.name} says Woof!"
    
    def hunger(self):
    
        return f"{self.name} says I'm HUNGRY!"
        