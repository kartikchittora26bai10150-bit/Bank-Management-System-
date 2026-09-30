

class BankAccount:
    def __init__(self, acc_no, acc_pin, acc_holder_name, balance=0):
        self.acc_no = acc_no
        self.acc_pin = acc_pin
        self.acc_holder_name = acc_holder_name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "deposited successfully.") 
        else:
            print("False amount.")
    def withdraw(self, amount):
        if amount <= 0:
            print("False amount.")
        elif amount > self.balance:
            print("Does not have sufficient balance.") 
            self.balance -= amount
            print(amount, "Taken money Successfully.") 
    def check_balance(self):
        print("Current Balance:", self.balance)
    def display_details(self):
        print("\n--- Account Details ---")
        print("Acc Number:", self.acc_no)
        print("Acc PIN:", self.acc_pin) 
        print("Acc Holder name:", self.acc_holder_name)
        print("Balance:", self.balance)
class Bank:
    def __init__(self):
        self.accounts = {} 
    def create_account(self):
        acc_no = input("Enter acc number: ")       
        if acc_no in self.accounts:
            print("Error: this account already exists.")
            return           
        acc_pin = input("Type Your PIN: ")
        name = input("Enter acc holder name: ")        
        initial_balance = float(input("Enter your first deposit: "))       
        if initial_balance < 0:
            print("False initial balance.")
            return       
        self.accounts[acc_no] = BankAccount(acc_no, acc_pin, name, initial_balance)
        print("Congratulations, your Account was created successfully.")
    def get_account(self):
        # helper to find and auth account
        acc_no = input("Enter acc number: ")       
        if acc_no not in self.accounts:
            print("Error: your Account was not found.")
            return None            
        account = self.accounts[acc_no]
        pin = input("Type your PIN: ")        
        if account.acc_pin == pin:
            return account
        else:
            print("Invalid PIN")
            return None
    def deposit_money(self):
        account = self.get_account()
        if account:
            amount = float(input("Type amount to Deposit: "))
            account.deposit(amount)
    def withdraw_money(self):
        account = self.get_account()
        if account:
            amount = float(input("Type amount to take out: "))
            account.withdraw(amount)
    def check_balance(self):
        account = self.get_account()
        if account:
            account.check_balance()
    def account_details(self):
        account = self.get_account()
        if account:
            account.display_details()

bank = Bank()
while True:
    print("\n BANK MANAGEMENT SYSTEM ")
    print("1. Create New Account")
    print("2. Submit Money")
    print("3. Take out Money")
    print("4. Check my Balance")
    print("5. Show my Account Details")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        bank.create_account()
    elif choice == '2':
        bank.deposit_money()
    elif choice == '3':
        bank.withdraw_money()
    elif choice == '4':
        bank.check_balance()
    elif choice == '5':
        bank.account_details()
    elif choice == '6':
        print("Thank you for using Bank Management System!")
        break
    else:
        print("Invalid choice. Please try again.")