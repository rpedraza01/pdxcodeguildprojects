#optional_lab_sock_sorter.py
import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
socks = {'ankle': 0, 'crew': 0, 'calf': 0, 'thigh': 0} #Dictionary of types of socks

#sock = {}
#for lines 11 - 14 and 16, they are different ways to reference the dictionary key in the empty dictionary in line 7
for i in range(100):
    sock = random.choice(sock_types)
    # if sock in socks:
    #   socks[sock] += 1
    #else:
    #   socks[sock] = 1
    socks[sock] += 1
    #socks[sock] = socks.get(sock, 0) + 1

print(socks)

for key in socks:
    #print(key)
    if socks[key] % 2 != 0:
        print(f"{key} has a loner.")
