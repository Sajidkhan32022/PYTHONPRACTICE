class Account:  # parent class
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self. amount= amount
        self.balance = self.balance - self.amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate / 100)


demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object
demo1.withdrawal(500)
print(demo1.getBalance())
a = [0, 1, 2, 3]
for a[-1] in a:
    print(a[-1])
print(['educative', 'fun'][bool('3')])