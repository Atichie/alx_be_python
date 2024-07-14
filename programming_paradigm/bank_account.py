class BankAccount:
    def _init_(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self,amount):
        """
        deposit specified amount to the account
        """
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount:2f}.")
        else:
            print("Deposit amount must be a positive.")

    def withdraw(self, amount):
        """
        withdraw specified amount to the account
        """
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"Withdraw ${amount:2f}.")
                return True
            else:
                print("Insufficient fund.")
                return False
        else:
            print("Withdrawn amount must be positive.")

    def display_balance(self, amount):
        """
        display_balance should print the current balance in a user-friendly format
        """
        print(f"Current balance ${amount:2f}.")

name = "main"
if name == "_main_":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(20)
    account.display_balance()


