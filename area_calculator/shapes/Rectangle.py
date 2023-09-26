import shapes.Shape as sh

class Rectangle(sh.Shape):
    def __init__(self, name,widht, height):
        super().__init__(name)
        self.width = widht
        self.height = height

    def calculate_area(self):
        return self.height * self.width