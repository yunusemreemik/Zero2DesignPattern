# Step 1: Strategy Interfaces
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")

# Step 2: Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, total_amount):
        self.payment_strategy.pay(total_amount)

# Step 3: Client Usage
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

cart1 = ShoppingCart(credit_card_payment)
cart1.checkout(100)  # Output: Paying 100 using Credit Card

cart2 = ShoppingCart(paypal_payment)
cart2.checkout(200)  # Output: Paying 200 using PayPal
