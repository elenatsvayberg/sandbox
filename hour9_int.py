students_grades = []
while True:
    data = {}
    data["student_name"] = input("Please give me the name of the student (q to quit): ")
    if data["student_name"] == 'q':
        break
    data["grade"] = input("Please give me their grade: ").capitalize()
    students_grades.append(data)

print("Okay, printing grades!")

for data in students_grades:
    print("{student_name}: {grade}".format(**data))


print()


students = {}
while True:
    name = input("Please give me the name of the student (q to quit): ")
    grade = input("Please give me their grade: ".capitalize())
    students[name] = grade
    if name == "q":
        print(students)
        break
