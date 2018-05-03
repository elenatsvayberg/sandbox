class MyClass(object):
    a = 9
    b = 7
new_item = MyClass()
new_item.a = 10
print(new_item.a)

if __name__ == "__main()__":
    main()

class MyClass1(object):
    a = 5
    b = 7
    def print_a(self):
        print("Hello! Here is a: {}" . format(self.a))
myobject = MyClass1()
myobject.print_a()

print()

class School(object):
    name = ""
    address = ""
    type = "grade school"
    def print_school(self):
        print(self.name)
        print(self.address)
        print("Type: " + self.type)
school1 = School()
school2 = School()

school1.name = "Columbia Middle school"
school1.address = "Berkeley Heights, NJ"
school2.name = "GL"
school2.address = "Berekeley Heights, NJ"
school2.type = "high"

school1.print_school()
print()
school2.print_school()

print()

class Student(object):
    def __init__ (self, name = "None", grade = "K", district = "Orange County"):
        self.name = name
        self.grade = grade
        self.district = district

student1 = Student()
student2 = Student (name = "Byron Blaze" , grade = "12", district = "Fairfax County")
print(student1.name)
print(student2.name)

print("_______________"*10)






