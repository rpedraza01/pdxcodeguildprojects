#atm_lab_25.py

class ATM:
    def __init__(self):
        # self.balance begins as the int 0
        self.balance = 0
        # self.transactions is an empty list
        self.transactions = []


    def check_balance(self):
        # returns the account balance
        return self.balance


    def deposit(self, amount_in):
        # deposits the given amount in the account
        self.balance += amount_in
        # the variable message is created with the f-string
        message = f"You've deposited +${amount_in}"
        # the list self.transactions is appended with the variable message
        self.transactions.append(message)
        # returns the variable message
        return message


    def check_withdrawl(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative
        return self.balance >= amount


    def withdraw(self, amount_out):
        # withdraws the amount from the account and returns it
        # creates the variable message with an f-string
        message = f"You've withdrawn -${amount_out}"
        # the list self.transactions is appended with the variable message
        self.transactions.append(message)
        # creates the if statement to see if there's enough money that can be withdrawn using the self.balance method to check if there's sufficient funds
        if self.check_withdrawl(amount_out):
            # if there's sufficient funds, money is withdrawn and the variable message is printed
            self.balance -= amount_out
            print(message)
        # if there's isn't enough funds to be withdrawn a statement stating such is printed
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


# the class ATM is called by creating the instance of atm
atm = ATM()


# a while True loop is created where the program is run outside of the classes and methods
while True:
    # prints a welcome statement
    print("Welcome to ATM.")
    # creates another while True loop
    while True:
        # creates the list of command which has the recognized strings for the user to enter to use the prorgam
        command = ["deposit", "withdraw", "check balance", "transaction history", "exit"]
        # creates the variable user_command which is modified by whatever command the user inputs
        user_command = input("What would you like to do today? (Deposit, Withdraw, Check Balance, Transaction History, Exit) > ")
        # prints the users command
        print(user_command)
        # an if loop is created that checks the user's command and executes it, checking that the command(s) are from the approved list in the variable command
        if user_command in command:
            if user_command == "deposit":
                print(atm.deposit(int(input("How much would you like to deposit? > "))))

            elif user_command == "withdraw":
                atm.withdraw(int(input("How much would you like to withdraw? > ")))

            elif user_command == "check balance":
                print(atm.check_balance())

            elif user_command == "transaction history":
                atm.print_transactions()
            # if an invalid command is inputted the loop breaks
            else:
                break
    break
