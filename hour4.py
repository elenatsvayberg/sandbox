s="Hello, world!"
print(len(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

birth_year = "1980"
state = "VA"
print(birth_year.isdigit())
print(state.isdigit())


first_name = "Elena"
last_name = "Tsvayberg"
print (first_name + " " + last_name)

s = "hello"
print(s*-5)

s = "66"
print(s*1)

a= "Virginia"
b= "virginina"
print (a==b)

rhyme = "Little Miss Muffet\n\
        Sat on atuffetn\n\
        Eating her curds and whey"
print(rhyme)

header = "Dish\tPrice\tType"
print(header)

name='Henty O\'Connor'
print(name)

path="C:\\users\\alex\\sandbox"
print (path)

f_name ="Hannah "
m_name = "Marie"
print(f_name + " " + m_name)
if f_name.strip() == "Hannah":
    print("Hi,", f_name)
else:
    print("Who are you?")
print()
bad_input = "***Hannah***"
print(bad_input.rstrip("*"))
print(bad_input.lstrip("*"))
print()
longtext = "hello ugly day"
print(longtext.count("ugly"))
print(longtext.find("2"))
print(longtext.replace("ugly","nice"))
print()
s="1"
print(type(s))

print()
print()
email="This is a joke"
if (email.find("emergency"))>0:
    print("Do you want to make this email urgent?")
elif (email.find("joke"))>0:
    print("Do you want to send this email as non-urgent?")