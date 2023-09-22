import animals.mammal as ml

class Cat(ml.Mammal):
    def __init__(self,name,age,fur_color,breed):
        super().__init__(name,age,fur_color)
        self.breed = breed
        
    def speak(self):
        
        return f"{self.name} says Meow!"
    
    def hunger(self):
        return f"{self.name} says I'm HUNGRY!"
        
        