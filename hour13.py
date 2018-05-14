import this
print(this)

from random import randint
for i in range(10):
    print(randint(1, 10))

frequency = {}
for i in range (1000):
    num = randint(1, 10)
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
print(frequency)
