class account:

    def __init__(self, account, balance):
        self.account_no = account
        self.balance = balance

    def debit(self, amount):
        self.balance -= amount
        print("BDT", amount, "was debited")
        print("total balance is = ",self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("BDT", amount, "was credited")
        print("total balance is = ", self.get_balance())
    def get_balance(self):
        print("Current Balance:", self.balance)



a1 = account(24235, 300000)

print(a1.balance)
print(a1.account_no)

a1.credit(1000)
a1.debit(500)






