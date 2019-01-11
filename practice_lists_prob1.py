#practice_lists_prob1.py
import random
def random_element(a):
    return a[random.randint(0, len(a) - 1)] # Or use return random.choice(a)
