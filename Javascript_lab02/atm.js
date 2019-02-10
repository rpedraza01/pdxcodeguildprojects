class ATM {
    constructor() {
        this.balance = 0;
        this.transactions = [];
    }

    check_balance() {
        return this.balance;
    }

    deposit(amount_in) {
        // alert(this.transactions)
        this.balance += parseFloat(amount_in);
        var message = `You've deposited +$${amount_in}`;
        alert(message)
        this.transactions.push(message);
        // alert(this.transactions);
        return message;
    }

    // check_withdrawl(amount) {
    //     return this.balance >= amount;
    // }

    withdraw(amount_out) {
        var message = `You've withdrawn -$${amount_out}`;
        this.transactions.push(message);
        if (amount_out < this.check_balance()) {
            this.balance -= parseFloat(amount_out);
            alert(message);
        }
        else {
            alert("Insufficient funds. Please withdraw an amount less than your account balance.");
        }
    }

    print_transactions() {
        for (line in this.transactions) {
            alert(line);
        }
    }

    atm_commands() {
        alert("Deposit.");
        alert("Withdraw.");
        alert("Check Balance.");
        alert("Transaction History.");
        var valid_commands = ["deposit", "withdraw", "check balance", "transaction history", "exit"];
    }
}

let atm = new ATM();
while (true) {
    alert("Welcome to ATM.");
    while (true) {
        var command = ["deposit", "withdraw", "check balance", "transaction history", "exit"];
        var user_command = prompt("What would you like to do today? (Deposit, Withdraw, Check Balance, Transaction History, Exit)");
        alert(user_command);
        // alert(command);
        if (command.includes(user_command)) {
            if (user_command === "deposit") {
                atm.deposit(prompt("How much would you like to deposit?"));
            }

            else if (user_command === "withdraw") {
                atm.withdraw(prompt("How much would you like to withdraw?"));
            }

            else if (user_command === "check balance") {
                alert(atm.check_balance());
            }

            else if (user_command === "transaction history") {
                alert(atm.print_transactions());
            }

            else {
                break;
            }
    break;
        }
    }
}