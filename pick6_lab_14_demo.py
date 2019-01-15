#pick6_lab_14_demo.py
import random

# Generates lottery ticket. Returns list of 6 randomly selected numbers between 1-99
def pick6():
    return [random.randint(1, 99) for i in range(6)]
    # Equivalent to above
    # ticket = []
    # for i in range(6):
        # ticket.append(random.randint(1, 99))
    # return ticket

# Calculates payout based on number of matches between a ticket and
def calculate_payout(winning, ticket):
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    # equivalent to above
    # payout = {"1 matching number": 4, "2 matching numbers": 7, "3 matching numbers": 100, "4 matching numbers": 50000, "5 matching numbers": 1000000, "6 matching numbers": 25000000}
    # payout [matches]
    matches = 0
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1

    matches = [winning[1] for i in range(len(winning)) if winning[i] == ticket[i]]
    # print("matches:", matches)
    # print("num matches:", len(matches))
    return payout[len(matches)]

def main():
    # 1. Generate a list of 6 random numbers representing the winning tickets
    # 2. Start your balance at 0
    # 3. Loop 100,000 times, for each loop:
    # 4. Generate a list of 6 random numbers representing the ticket
    # 5. Subtract 2 from your balance (you bought a ticket)
    # 6. Find how many numbers match
    # 7. Add to your balance the winnings from your matches
    # 8. After the loop, print the final balance
    winning = pick6()
    balance = 0

    for i in range(100000):
        print("balance:", balance)
        print("winning:", winning)
        ticket = pick6()
        print("ticket:", ticket)
        balance -= 2
        winnings = calculate_payout(winning, ticket)
        balance += payout

    print("balance:", balance)
    # print(winning)
    # print(calculate_payout([1,2,3,4,5,6], [1,2,3,4,5,6]))
