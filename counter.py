#Tyler Vultaggio
#Lab 9 - Working with Objects and Inheritance
#11/19/2019


class Counter:
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1
        
    def clear(self):
        self.count = 0
        
    def get_value(self):
        return self.count

class BankAccount:
    """Bank Account protected by a pin number."""
    
    def __init__(self, pin):
        """Initial account balance is 0 and pin is 'pin'."""
        
    def deposit(self, pin, amount):
        """Increment account balance by amount and return new balance."""
        
    def withdraw(self, pin, amount):
        """Decrement account balance by amount and return amount withdrawn."""
        
    def get_balance(self, pin):
        """Return account balance."""
        
    def change_pin(self, oldpin, newpin):
        """Change pin from oldpin to newpin."""
