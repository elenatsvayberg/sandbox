def main():
    class_list=["Elena", "Alex", "Shelly"]
    greeting()
    check_user(class_list)
    goodbye()

def greeting():
    print("Welcome to the student checker!")

def goodbye():
    print("Googbye!")

def check_user(class_list):
    while True:
        inp=input("Please give me the name of the student( enter \'q\' to quit : ")
        if inp =='q':
            break
        if inp in class_list:
            print("Yes, that student is enrolled in the class!")
        else:
            print("No, that student is not in the class.")

if __name__== "__main__":
    main()