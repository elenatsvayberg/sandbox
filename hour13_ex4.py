from random import random
count = 0

while True:
    number = random()
    test_num = input("Test random number [Y,N}")
    if test_num =="Y":
        print(number)
        count = count+1
        print(count)
    elif test_num=="N":
        print("Total times of testing= " + "{}" .format(count))
        break