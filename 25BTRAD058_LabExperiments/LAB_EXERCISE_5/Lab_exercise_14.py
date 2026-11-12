#Bank account system using OOP.
#* Bank Account System Using OOP: Develop a Python program using classes and objects to manage bank
#accounts. Implement deposit, withdrawal, balance enquiry, and transaction validation
# * Design appropriate classes and methods, apply encapsulation, analyze transaction conditions, and test
# invalid transactions and insufficient balances.
# * Simulate routine banking transactions and explain how object-oriented programming supports account management and data protection.

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def display(self):
        print("Balance:", self.__balance)
b = Bank(1000)
b.deposit(500)
b.withdraw(200)
b.display()