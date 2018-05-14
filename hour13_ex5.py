from random import randint
print("Welcome to the number  guessing game: ")
print("I have my number")
number = randint(1, 5)
while True:
     inp = int(input("What is your guess[1 - 5] : "))
     if inp == number:
        print("You got it! Thanks for playing! Number is " "{}". format(inp))
        break
     elif inp>number:
        print("That's too high. Try again")
     elif inp<number:
        print("That's too low. Try again.")