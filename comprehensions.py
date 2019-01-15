#comprehensions.py
one_to_ten = [i for i in range(1, 11)]
## equivalent to above
# one_to_ten = []
# for i in range(1, 11):
#    one_to_ten.append(i)

print(one_to_ten)

# map
doubled = [x * 2 for x in one_to_ten] #mapping all the elements to a value of another
## equivalent to above
# doubled = []
# for x in one_to_ten:
#    doubled.append(x*2)
print(doubled)

#filter
evens = [x for x in one_to_ten if x % 2 == 0]
## equivalent to above
# evens = []
# for x in one_to_ten:
#    if x % 2 == 0:
#        evens.append(x)
print(evens)

odds_plus_ten = [x + 10 for x in one_to_ten if x % 2 != 0]
print(odds_plus_ten)

# nested comprehensions aka comprehensions inside of other comprehensions
# board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 5
columns = 6
board = []
for row in range(rows):
    row = []
    for column in range(columns):
        row.append(column)
    board.append(row)

board = [[col for col in range(6)] for row in range(5)]

print(board)

# dictionary comprehensions
fruits = {"a": "apples", "b": "bananas", "c": "coconuts"}
fruits_capitalized = {k.upper(): v.upper() for (k,v) in fruits.items()}
print(fruits_capitalized)

fruits_without_a = {k:v for k,v in fruits.items() if v.find("a") == -1}
print(fruits_without_a)
