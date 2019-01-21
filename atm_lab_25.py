#atm_lab_25.py

class ATM:
    def __init__(self):
        # self.balance begins as 
        self.balance = 0
        self.transactions = []

    def check_balance(self):
        # returns the account balance
        return self.balance

    def deposit(self, amount_in):
        # deposits the given amount in the account
        self.balance += amount_in
        message = f"You've deposited +${amount_in}"
        self.transactions.append(message)
        return message


    def check_withdrawl(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative
        return self.balance >= amount


    def withdraw(self, amount_out):
        # withdraws the amount from the account and returns it
        message = f"You've withdrawn -${amount_out}"
        self.transactions.append(message)
        if self.check_withdrawl(amount_out):
            self.balance -= amount_out
            print(message)
        else:
            print("Insufficient funds. Please withdraw an amount less than your account balance.")


    def print_transactions(self):
        # prints out the list of transactions
        for line in self.transactions:
            print(line)
        # print(self.transactions)


    def atm_commands():
        print("Deposit.")
        print("Withdraw.")
        print("Check Balance.")
        print("Transaction History.")
        valid_commands = ["deposit", "withdraw", "check balance", "transaction history", "exit"]

atm = ATM()
# print(atm.balance)
# atm.check_balance()
# print(atm.check_balance())
# print(atm.deposit(10))
# print(atm.balance)
# atm.check_withdrawl(10)
# print(atm.balance)
# atm.withdraw(5)
# print(atm.balance)
# atm.print_transactions()
# print(atm.print_transactions())

while True:
    print("Welcome to ATM.")
    while True:
        command = ["deposit", "withdraw", "check balance", "transaction history", "exit"]
        user_command = input("What would you like to do today? (Deposit, Withdraw, Check Balance, Transaction History, Exit) > ")
        print(user_command)
        if user_command in command:
            if user_command == "deposit":
                print(atm.deposit(int(input("How much would you like to deposit? > "))))

            elif user_command == "withdraw":
                atm.withdraw(int(input("How much would you like to withdraw? > ")))

            elif user_command == "check balance":
                print(atm.check_balance())

            elif user_command == "transaction history":
                atm.print_transactions()

            else:
                break
    break

# tests