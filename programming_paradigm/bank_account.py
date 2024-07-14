class BankAccount:
    def __init__ (self, initial_balance):
        self.account_balance = float(initial_balance=0.0)

    def deposit(self,amount):
            self.account_balance += float(amount)
            return self.account_balance

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= float(amount)
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:2f}.")

name = "main"
if name == "_main_":
    account = BankAccount(250)
    account.dispay_balance()
    account.deposit(50)
    account.dispay_balance()

    account.withdraw(20)
    account.dispay_balance()

    success = account.withdraw(200)
    print(f"Withdrawal successful: {success}")

    account.display_balance()


