stock = ['pepperoni', 'sausage', 'cheese', 'peppers']
new=[]
for num in range(2):
    top = input("Please give me a topping: ")
    if top in stock:
        print("We have {}" .format(top))
    else:
        print("We don't have {}" .format(top))
        new.append(top)
print("Here are your toppings: {}" .format(stock))
print("New list {}" .format(new))


