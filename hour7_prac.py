print("Welcome to the receipt program!")
total = 0
while True:
    inp = input("Enter the value for the seat[\'q\' to quit]:")
    if inp.isdigit():
        total = total + float(inp)
    elif inp == 'q':
            break
    else:
        print("i\'m sorry, but {} isn\'t valid. Please try gain" .format(inp))

print("Total: {} ". format(total))


