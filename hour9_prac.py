def key():
    student_list{}
     while True:
        key = input("Please give me name of the student (q to quit): ")

        if key == 'q':
           break

        else:
            return key
            value = input("Please give me their grade : ")
            if value.upper() in ["A", "B", "C", "D"]:
               return value.upper()

            else:
                print("Correct grade. {} isn\'t valid" .format(value))


def main():
    #student_list={}
    name=key()
    grade= value()
    #student_list= {"Student1" : "A",
    #               "Student2" : "B",
    #              "Student3" : "C",
    #               "Student4" : "D"}
    #student_list[names] = grade

    print("\tStudent \tGrade")
    print(student_list.keys())
    print (student_list.values())
    #print(student_list)

if __name__ == "__main__":
    main()