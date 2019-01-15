#practice_lists_03.py
def eveneven(numbers):
    # numbers = [1,2,3,4,5,6]
    evens = 0
    # evens = [num for num in numbers if num % 2 == 0]
    # retun len(evens) % 2 == 0
    # equivalent to line 5 and 6
    # evens = []
    # for num in numbers:
    #   if num % 2 == 0:
    #       evens.append(num)
    # return len(evens) % 2 == 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        evens += 1
return evens % 2 == 0

eveneven(numbers)
