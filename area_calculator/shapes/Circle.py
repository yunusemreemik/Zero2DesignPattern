import shapes.Shape as sh

class Circle(sh.Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.raidus = radius

    def calculate_area(self):
        return 3.14 * self.raidus**2