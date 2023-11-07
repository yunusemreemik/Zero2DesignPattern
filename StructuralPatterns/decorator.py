# Step 1: Define the Component interface
class Coffee:
    def cost(self):
        return 5  # Base cost of a plain coffee

# Step 2: Create ConcreteComponent implementing the Component interface
class PlainCoffee(Coffee):
    def cost(self):
        return super().cost()

# Step 3: Create Decorator interface (Optional)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Step 4: Create ConcreteDecorator classes implementing the Decorator interface
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2  # Additional cost for milk

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1  # Additional cost for sugar

# Step 5: Client code using decorators
plain_coffee = PlainCoffee()
print("Cost of Plain Coffee:", plain_coffee.cost())  # Output: 5

milk_coffee = MilkDecorator(plain_coffee)
print("Cost of Coffee with Milk:", milk_coffee.cost())  # Output: 7

sugar_milk_coffee = SugarDecorator(milk_coffee)
print("Cost of Coffee with Milk and Sugar:", sugar_milk_coffee.cost())  # Output: 8
