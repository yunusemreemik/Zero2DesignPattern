from typing import Any


class BankAccount:
    def __init__(self,account_holder,balance=0) -> None:
        self.account_holder = account_holder
        self.__balance = balance #encapsulation
        pass

    def depoist(self, amount):
        if amount > 0:
            self.__balance += amount
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance 
    
my_account = BankAccount("Aleyna")
my_account.depoist(1000)
my_account.withdraw(500)
print(my_account.get_balance())

        