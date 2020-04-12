from random import randint
import sys

alphabet = "ABCDEFGHIJKLMNOPRSTUVWCYZ"
a_size = len(alphabet) - 1 
count = int(sys.argv[1])
try:
    max_size = sys.argv[2]
except:
    max_size = 1000
results = []
for i in range(0, count):
    size = randint(1, max_size)
    k = randint(1, int(size * 0.7))
    string = ""
    change = True
    for j in range(0, size):
        if change:
            letter_index = randint(0, a_size)
        change = randint(0, 2) < 1
        string += alphabet[letter_index]
    results.append((string, k))

with open('tests.txt', 'w') as f:
    f.write(str(results))
# print(results)