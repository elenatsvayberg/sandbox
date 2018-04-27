def print_total(customer_name, items):
    print("Total for {}" .format(customer_name))
    total = 0
    for item in items:
        total = total + item
    print("Total {}" .format(total))
print_total(customer_name = "Elena", items = [5, 6, 7])
print()
def print_welcome(first, last, middle = " "):
    print("Welcome, {} {} {}" .format(first, middle, last))
    print("Enjoy your stay!")
print_welcome(first= "James", last= "Grinelly")

def get_total(items):
    total = 0
    for item in items:
        total = total + item
        return total
items= [2.5, 6.3, 8.5]
print("Total {}".format(get_total(items)))
print()
def get_res(number):
    square = number **2
    cube = number ** 3
    return square, cube

square, cube = get_res(5)
print(square)
print(cube)
print()
def check_year(year):
    if len(year) !=4:
        print("{} is an invalid year entry!".format(year))
        return
    print("Good that seems to work as a year!")

check_year("1975")

def main():
    user = get_username()
    password = get_password()
    authenticated = authenticate(user = username, password = password)
    if (authenticated):
        print_timesheet(username)
        add_hours(username)

#if __name__ == "__main__":
#__name__

def test(item_one, item_two, **kwargs):
    print(item_one)
    print(item_two)
    print(kwargs)
test(item_one= "Hello", item_two = "world", item_three = "How are you?", item_five = "test")

def test(item_one, item_two, *args):
    print(item_one)
    print(item_two)
    print(args)
test(1,2,3,4,5,)