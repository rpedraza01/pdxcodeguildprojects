class ATM {
    constructor() {
        this.balance = 0;
        this.transactions = [];
    }

    check_balance() {
        return this.balance;
    }

    deposit(amount_in) {
        this.balance += parseFloat(amount_in);
        var message = `You've deposited +$${amount_in}`;
        // alert(message);
        this.transactions.push(message);
        return message;
    }

    withdraw(amount_out) {
        var message = `You've withdrawn -$${amount_out}`;
        this.transactions.push(message);
        if (amount_out < this.check_balance()) {
            this.balance -= parseFloat(amount_out);
            // alert(message);
        }
        else {
            alert("Insufficient funds. Please withdraw an amount less than your account balance.");
        }
    }

    print_transactions() {
        alert(this.transactions);
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

var ul = document.createElement("ul");
let body = document.getElementsByTagName("body")[0];
let balance = document.getElementById("balance");

let depositButton = document.querySelector("#depositButton");
depositButton.addEventListener("click", function() {
    let depositField = document.getElementById("depositInput");
    let depositInput = depositField.value;
    // console.log(depositInput);
    atm.deposit(depositInput);
    balance.innerText = `Your Balance is $${atm.check_balance()}`;
    var li = document.createElement("li");
    li.innerText = `+$${depositInput}`;
    // console.log(li);
    ul.appendChild(li);
    // console.log(ul);
    depositField.value = "0";
});

// let balanceButton = document.querySelector("#balanceButton");
// balanceButton.addEventListener("click", function() {
//     alert(`Your balance is $${atm.check_balance()}`);
// });

let withdrawButton = document.querySelector("#withdrawButton");
withdrawButton.addEventListener("click", function() {
    let withdrawField = document.getElementById("withdrawInput");
    let withdrawInput = withdrawField.value;
    atm.withdraw(withdrawInput);
    balance.innerText = `Your Balance is $${atm.check_balance()}`;
    var li = document.createElement("li");
    li.innerText = `-$${withdrawInput}`;
    ul.appendChild(li);
    withdrawField.value = "0";
});

// let transactionButton = document.getElementById("transactionButton");
// transactionButton.addEventListener("click", function() {
//     alert(atm.print_transactions());
// });

body.appendChild(ul);