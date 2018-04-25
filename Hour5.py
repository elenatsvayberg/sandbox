age = input("Enter your age: ")
age=int(age)
print(age)

print()
#password
#from getpass import getpass
#password = getpass("Please enter password: ")

year = input("What year were you born: ")
if len(year)!=4 or not year.isdigit():
    print("I'm sorry , I don't like that nuimber. ")
else:
    print("That is a good number. Moving on!")

address = input("Enter address:")
address = address.strip()
print(address)

print()
greeting = "Good {}, {}. How are you today?"
name = "Elena"
time = "afternoon"
print(greeting.format(time, name))

print()
special_text = "Good {time}! Today's specials are: {special1} and {special2}."
time = "afternoon"
food1 = "spam with eggs"
food2 = "eggs with spam"
print (special_text.format(time=time, special1 = food1, special2 = food2))

print()
line = "Cities with Python meet ups: {0},{1},{2}"
print(line.format("District oF Columbia", " Portland", " and many more!", "abc"))

print()
fruit = "Types of fruit: {}, {}, and {}"
print(fruit.format("apple", "pear", "peach", "coconut"))

