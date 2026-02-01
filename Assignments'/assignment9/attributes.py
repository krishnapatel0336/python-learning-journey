class foodItem:
    category="snacks"
    def __init__(self, name):
        self.name =name

snacks1= foodItem("Samosa")
snacks2= foodItem("GulabJamun")
print("FooD1 :", snacks1.name)
print("FooD2 :", snacks2.name)

# Create account class with attributes and methods

class Account:
    def __init__(self, accountNumber, balance):
        self.aC= accountNumber
        self.balance= balance

    def credit(self , amount):
        self.balance += amount
        print("Amount credited:",amount)

    def debit(self, amount):
        self.balance -= amount
        print("Amount debited:", amount)

    def net_balance(self):
        print("Amount:", self.aC, "| Balance:", self.balance)
        
a1=Account("Saumya1Singh", 50000)
a1.credit(1000)
a1.debit(500)
a1.net_balance()





