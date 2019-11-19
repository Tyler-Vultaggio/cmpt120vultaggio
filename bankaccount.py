#Tyler Vultaggio
#Lab 9 - Working with Objects and Inheritance
#11/19/2019


class BankAccount:
    #"""Bank Account protected by a pin number."""
    
    def __init__(self, pin):
        #"""Initial account balance is 0 and pin is 'pin'."""
        self.pin = pin
        self.bal = 0
        
    def deposit(self, pin, amount):
        #"""Increment account balance by amount and return new balance."""
        if pin == self.pin:
            self.bal += amount
        
    def withdraw(self, pin, amount):
        #"""Decrement account balance by amount and return amount withdrawn."""
        if pin == self.pin:
            self.bal -= amount
                
    def get_balance(self, pin):
        #"""Return account balance."""
        if pin == self.pin:
            return self.bal
        
    def change_pin(self, oldpin, newpin):
        #"""Change pin from oldpin to newpin."""
        if oldpin == self.pin:
            self.pin = newpin
        return self.pin
