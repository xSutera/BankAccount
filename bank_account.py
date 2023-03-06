class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        # your code here
        self.balance+=amount
        return self
    def withdraw(self, amount):
        # your code here
        if(self.balance<amount):
            print("Insufficient Funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance+=amount
        return self
    def display_account_info(self):
        # your code here
        print('Balance: '+str(self.balance))
        return self
    def yield_interest(self):
        # your code here
        if(self.balance>0):
            self.balance*=self.int_rate
        return self

User1=BankAccount(1.8,500)
User1.deposit(80).deposit(80).deposit(80).display_account_info()
User2=BankAccount(1.8,500)
User2.deposit(80).deposit(80).withdraw(85).withdraw(25).withdraw(5).withdraw(10).yield_interest().display_account_info()