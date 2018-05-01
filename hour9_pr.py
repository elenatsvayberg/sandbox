students = {}
while True:
    name = input("Enter student name otherwise input q: ")
    if name =='q':
        break
    else:
        grade = (input("Enter letter grade:")).capitalize()
        students[name] = grade
print(students)
