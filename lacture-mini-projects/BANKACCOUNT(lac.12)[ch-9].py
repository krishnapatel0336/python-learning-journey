class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 1000000
        self.logs = []

    def credit(self, amount):
        self.balance += amount
        self.logs.append(f"Credited: {amount}")

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.logs.append(f"Debited: {amount}")
        else:
            self.logs.append(f"Failed Debit: {amount} (Insufficient Funds)")

    def get_balance(self):
        return self.balance

    def get_logs(self):
        return self.logs
    
Customer1= BankAccount("SaumyaSingh")
print("Initial Balance:",Customer1.balance)
Customer1.credit(20000)
Customer1.debit(1000)
print( "FInale Balance", Customer1.get_balance())
print(Customer1.get_logs())





