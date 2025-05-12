class Bank:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Taka", amount, "was debited.")
        print("Total Balance = ", self.get_bal())

    def credit(self, amount):
        self.balance += amount
        print("Taka", amount, "was credited.")
        print("Total Balance = ", self.get_bal())

    def get_bal(self):
        return self.balance

p1 = Bank(10000, 101)
p1.debit(1000)
p1.credit(6000)
p1.debit(4000)
