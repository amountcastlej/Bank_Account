class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate=.01
        self.account_balance=0
    def deposit(self, amount):
        # increases the account balance by the given amount
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        # decreases the account balance by the given amount if there are sufficient funds
        # if there is not enough money, print a message: "insufficient funds: Charging a $5 fee and deduct $5"
        if self.account_balance - amount < 0:
            print(f"Insufficient Funds: Charging a $5 fee")
            self.account_balance -= 5
        else: 
            self.account_balance -= amount
            return self
    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
        return self
    def yield_interest(self):
        # increases the account balance by the current balance * the interest rate
        if self.account_balance > 0:
            new_bal = self.account_balance + (self.account_balance * int_rate)
            return self
    
# checking_account = BankAccount("0.1", "0")
# checking_account.deposit(200).display_account_info().deposit(300).display_account_info().deposit(400).display_account_info().withdraw(300).display_account_info()
savings_account = BankAccount("0.1", "0")
savings_account.deposit(500).display_account_info().deposit(9000).display_account_info().deposit(10000).display_account_info().withdraw(10000).display_account_info()



