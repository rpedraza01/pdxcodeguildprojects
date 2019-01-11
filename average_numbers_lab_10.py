#average_numbers_lab_10.py
def average(numbers):
    running_sum = 0
    for num in numbers:
        #int(input("Please enter your numbers. > "))
        #print(num)
        running_sum = (running_sum + num)
    print(running_sum / len(numbers))

nums = []
while True:
    num = input('Enter a number or "done"')
    if num == 'done':
        break
    nums.append(int(num))

average(nums)
