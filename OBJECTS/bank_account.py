# create a bank account class with methods to display balance, make a deposit, and
# withdraw money

class BankAccount(object):

    def __init__(self, balance=0.0):
        self.balance = balance


    def display_balance(self):
        print(f"Your balance is {self.balance}")

    # THIS METHOD ASKS USER FOR INPUT, CHECKS IF THE AMOUNT IS GREATER THAN THE BALANCE AND THEN
    # INCREMENT BALANCE
    def make_deposit(self):
        amount = float(input("How much would you like to deposit? >>> "))
        self.balance += amount
        print(f"Balance is now {self.balance}")

    # THIS METHOD ASKS USER FOR INPUT, CHECKS IF AMOUNT UIS GREATER THAN THE BALANCE AND SHOWS FUNDS
    # OTHERWISE IT DECREMENTS THE BALANCE
    def make_withdrawal(self):
        amount = float(input("How much money would you like to withdraw? >>> "))
        if amount > self.balance:
            print(f"You do not have sufficient funds. Your balance is {self.balance}.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful: balance is now {self.balance}")

        
bank_user = BankAccount(1000.00)
bank_user.display_balance()
bank_user.make_deposit()
bank_user.make_withdrawal()

