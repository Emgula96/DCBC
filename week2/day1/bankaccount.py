# Create a class called BankAccount.
# Add properties for balance and account_number
# Allow the user to deposit funds to the account. This can be accomplished by adding a deposit function to the BankAccount class.
# Allow the user to withdraw funds from the account. This can be accomplished by adding a withdraw function to the BankAccount class.
# Allow the user to transfer funds between two accounts. This can be accomplished by adding a transfer_funds function to the BankAccount class.
# After creating the BankAccount class, along with all the functions make sure to create instance of BankAccount and perform actions.

class bankAccount:
    def __init__(self, balance, accntNum):
        self.balance = balance
        self.accntNum = accntNum

    def deposit(self, funds):
        self.balance += funds
        print(f'You deposited ${funds} into {self.accntNum} account')

    def withdrawl(self, funds):
        self.balance -= funds
        print(f'You withdrew ${funds} from {self.accntNum} account')

    def transferFunds(self, Accnt, funds):
        self.withdrawl(funds)
        Accnt.deposit(funds)

ethanChecking = bankAccount(10_000, 1112223344)
# print(balanceChecking.balance)

# balanceChecking.deposit(1300)
# print(balanceChecking.balance)

# balanceChecking.withdrawl(500)
# print(balanceChecking.balance)

ethanSavings = bankAccount(20000, 99988877)
ethanChecking.transferFunds(ethanSavings, 1000)

print(ethanChecking.balance)
print(ethanSavings.balance)



# class BankAccount:
#     def __init__(self, account_number):
#         self.account_number = account_number
#         self.balance = 0
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         self.balance -= amount
#     def transfer_funds(self, transferFrom, transferTo, amount):
#         transferFrom.withdraw(amount)
#         transferTo.deposit(amount)
#     def __str__(self):
#         return f"{self.account_number}\n{self.balance}"

# checking_account = BankAccount("Checking")
# savings_account = BankAccount("Savings")

# checking_account.deposit(1000)
# checking_account.transfer_funds(checking_account, savings_account, 500)

# print(checking_account)
# print(savings_account