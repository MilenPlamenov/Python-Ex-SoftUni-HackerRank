class Account:
    def __init__(self, id, name, balance=None):
        self.id = id
        self.name = name
        if balance != None:  # balance - optional parameter !
            self.balance = balance
        else:
            self.balance = 0

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())