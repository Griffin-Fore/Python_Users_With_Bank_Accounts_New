class BankAccount:
    all_accounts = []

    def __init__(self, balance = 100, interest_rate = 0.05):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print(f"Depositting {amount}")
        self.balance += amount
        print(f"Balance: {self.balance}")

        return self

    def withdraw(self, amount):
        if(amount <= self.balance):
            print(f"Current Balance: {self.balance}.")
            print(f"Withdrawing {amount}.")
            self.balance -= amount
            print(f"New balance: {self.balance}")
        else:
            print(f"Attempting to withdraw {amount} from {self.balance}")
            print("Insufficient funds: Charging a $5 fee ")
            self.balance -= 5
            print(f"Balance after fee: {self.balance}")

        return self
    
    def display_account_info(self):
        print("Displaying account info")
        print(f"Account balance: {self.balance}")
        print(f"Account interest rate: {self.interest_rate}")
        
        return self

    def yield_interest(self):
        print("Yielding interest")
        print(f"Interest rate: {self.interest_rate}, Current balance: {self.balance}")
        self.balance *= (1 + self.interest_rate)
        print(f"New balance: {self.balance}")

        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print(account.balance)
            print(account.interest_rate)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance=500,interest_rate=0.02)

    def make_deposit(self, amount,):
        self.account.deposit(amount)
        print(f"Made a deposit of {amount}. Balance: {self.account.balance}")
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(f"Made a withddrawal of {amount}. Balance: {self.account.balance}")
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self
    
    def transfer_monney(self, amount, other_user):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)

User_1 = User("Griff","g@g.com")
User_1.display_user_balance().make_deposit(500).make_withdrawal(300)
User_2 = User("Girff","e@g.com")
User_2.display_user_balance().make_deposit(300).make_withdrawal(700)
User_1.transfer_monney(200,User_2)

# Account_1 = BankAccount()
# Account_1.display_account_info()
# Account_1.deposit(60).deposit(70).withdraw(40).yield_interest().display_account_info()
# Account_1.display_account_info()

# Account_2 = BankAccount(150, 0.06)
# Account_2.display_account_info().deposit(50).deposit(50).withdraw(30).withdraw(30).withdraw(30).withdraw(30).yield_interest().display_account_info()

# BankAccount.print_all_accounts()