"""Q5: Create a class BankAccount with:
 Class variable bank_name
 Instance variables account_holder and balance
Track how changing class and instance variables behave across different objects."""
class BankAccount:
    bank_name = "Rajput Bank"

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited amount: {amount}, New Balance:{self.balance}")
       
    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance -= amount
            print(f"Withdraw:{amount}, New Balance: {self.balance}")
        else:
            print("Insufficient Funds!")
    def display_account(self):
        print(f"Account Holder Name: {self.account_holder}")
        print(f"Bank Name: {BankAccount.bank_name}")
        print(f"Balance: {self.balance}")

account1 = BankAccount("Rakesh", 1000)
account2 = BankAccount("Rohan", 2000)

account1.deposit(500)
account2.withdraw(1500)

BankAccount.bank_name = "Rajputana Bank"

account1.display_account()
account2.display_account()