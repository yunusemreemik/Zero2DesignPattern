from abc import ABC, abstractmethod
class Product:
    def __init__(self):
        self.part1 = None
        self.part2 = None

class Builder(ABC):
    @abstractmethod
    def build_part1(self):
        pass

    @abstractmethod
    def build_part2(self):
        pass

    @abstractmethod
    def get_product(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part1(self):
        self.product.part1 = "Part 1 Built"

    def build_part2(self):
        self.product.part2 = "Part 2 Built"

    def get_product(self):
        return self.product

class Director:
    def construct(self, builder):
        builder.build_part1()
        builder.build_part2()

builder = ConcreteBuilder()
director = Director()
director.construct(builder)
product = builder.get_product()
print(product.part1)  # Output: Part 1 Built
print(product.part2)  # Output: Part 2 Built
