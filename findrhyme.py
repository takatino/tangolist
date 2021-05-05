import random

f = open(r'tangolist\tangolist.txt', 'r')
lines = f.readlines()
max_lines = len(lines)
f.close()

for i in range(3):
    i = random.randint(0, max_lines)
    print(lines[i].split(",")[0])

