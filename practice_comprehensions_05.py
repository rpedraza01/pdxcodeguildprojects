#practice_comprehensions_05.py
n = 10
def powers_of_two(n):
    print("n in function", n)
    return [2**i for i in range(n)]

print(powers_of_two(5))
print("n in main", n)

x = 0
def looping():
    x = 10 # local x
    print("x in function", x)
    for x in range(10): # local x
        print("x in function", x)
    print("x in function", x)

looping()
print("x in main", x)
