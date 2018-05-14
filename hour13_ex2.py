import random
print(random.randint(1,100))
print()

from random import random
for i in range(10):
    print(random())
print()

from random import uniform
for i in range(10):
    print(uniform(1,5))
print()

from random import choice
names = ["Hannah", "Jacob", "Jim", "Katie", "Josh"]
print(choice(names))
print(choice(names))
print(choice(names))

#help(choice)

from datetime import time
lunch = time(11,30)
#lunch datetime.time(11, 30)
print(lunch)
print(lunch.hour)
print(lunch.minute)
print(lunch.second)
#print("Lunch will be served at {minutes} minutes past {hour}". format (minutes = lunch.minute, hour = lunch.hour))
breakfast = time(7,10)
elevesies = time(11,30)
print(breakfast > lunch)
print(breakfast < lunch)
print(elevesies ==lunch)

import datetime
hm = datetime.datetime(year = 2018, day = 10, month = 5)
jt = datetime.datetime(year = 2018, day = 30, month = 12)
print(jt - hm)

week = datetime.timedelta(days = 7)
n = datetime.datetime.now()
print(n+week)

