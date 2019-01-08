# grading_lab_03.py
print("Let's figure out your grade.")
grade = input("Please enter your score, between 0 - 100 > ")
grade = int(grade)
#A = 90 <= 100
#B = 80 <= 89
#C = 70 <= 79
#D = 60 <= 69
#F = 0 <= 59
if grade >= 90:
    print("Great job, you get an 'A'!")
#elif grade >= 93 and grade <= 96.99
elif grade >= 80 and grade <= 89:
    print("Not bad, you get a 'B'!")
elif grade >= 70 and grade <= 79:
    print("Ok, you get a 'C'.")
elif grade >= 60 and grade <= 69:
    print("Looks like you could study some more, you get a 'D'.")
elif grade <= 59:
    print("Sorry, you get an 'F'.")
