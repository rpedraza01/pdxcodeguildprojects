#pick6_lab_14.py
import random

def pick6():
    # return [random.randint(1, 99) for i in range(6)]
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

def calculate_payout(winning, ticket):
    """ returns payout based on number of matching numbers between winning and ticket
    1. loop through tickets
    2.      if winning[i] == tickets[i], increase matches
    3. calculate payout based on matches
    4. return payout
    """
    for 
    pass


def play100k():
    winning = pick6()
    # winning = []
    # for i in range(6):
    #     winning.append(random.randint(1, 99))
    balance = 0
    for i in range(100000):
        ticket = pick6()
        # ticket = []
        # for i in range(6):
        #     ticket.append(random.randint(1, 99))        
        balance -= 2
        payout = calculate_payout(winning, ticket)
        balance += payout

    print("balance:", balance)


print("Let's make you rich today with Pick 6!")
print(calculate_payout([1,1,1,1,1,1], [1,1,1,1,1,2]))
# play100k()

