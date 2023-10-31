from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def create(self):
        pass

class ConcreteProductA(Product):
    def create(self):
        print("Product A Created")

class ConcreteProductB(Product):
    def create(self):
        print("Product B Created")

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create_product(self):
        product = self.factory_method()
        product.create()

class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()
    

creatorA = ConcreteCreatorA()
creatorA.create_product()  # Output: Product A Created

creatorB = ConcreteCreatorB()
creatorB.create_product()  # Output: Product B Created
