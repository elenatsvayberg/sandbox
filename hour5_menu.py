breakfast_special = "Texas Omelet"
breakfast_notes = "Contains brisket, horse radish cheddar"
lunch_special = "Greek patty melt"
lunch_notes = "Like the regular one, but with tzaziki sauce"
dinner_special = "Buffalo stake"
dinner_notes = "Top loin with hot sauce and blue cheese. NOT BUFFALO MEAT."

mealtime = input("Which mealtime do you want?: [breakfast, lunch, dinner]")
print("Specials for {}:".format(mealtime))
if mealtime.lower() == "breakfast":
    print(breakfast_special)
    print(breakfast_notes)
elif mealtime == "lunch":
    print(lunch_special)
    print(lunch_notes)
elif mealtime == "dinner":
    print(dinner_special)
    print(dinner_notes)
else:
    print("Sorry, {} isn\'t valid".format(mealtime))



name = input("Give me your name please:")
num = int(input("How many widgets are you buying?: "))
price = int(input("How much do they cost  per item? :"))
print( "Your total number {}, and cost ${}".format(num, price))
print("Total price $", num * price)
print("Thanks for shopping, " + name)