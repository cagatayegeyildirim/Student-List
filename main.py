from email.mime import application
from os import system
import json


class Student:
    def __init__(self, name, lastname, age, sex, major):
        self.__firstname = name
        self.__lastname = lastname
        self.__age = age
        self.__sex = sex
        self.__major = major

    def getFirstName(self):
        return self.__firstname

    def setFirstName(self, firstname):
        self.__firstname = firstname

    def getLastName(self):
        return self.__lastname

    def setLastName(self, lastname):
        self.__lastname = lastname

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def getSex(self):
        return self.__sex

    def setSex(self, sex):
        self.__sex = sex

    def getMajor(self):
        return self.__major

    def setMajor(self, major):
        self.__major = major


students = []
for x in range(10):
    fake_student = Student("studentname" + str(x), "studentsurname" +
                           str(x), 30 + x, 'F', 'Student')
    students.append(fake_student)
student1 = Student("x", "y", 22, 'F', 'Student')
students.append(student1)
student2 = Student("Cagatay Ege", "Yildirim", 21, 'M', 'Student')
students.append(student2)


while True:
    print("-----------------------------------------------------------------")
    print("1. Add a new student")
    print("2. Find a student by first name and last name")
    print("3. Show all students(all the information about them)")
    print("4. Show all students(in a given age range)")
    print("5. Modify a student record")
    print("6. Delete a student with a specific first name-last name")
    print("7. Write the contents of the student array to a file")
    print("8. Read student data from a file and populate the student array.")
    print("9. Quit")
    print("-----------------------------------------------------------------")
    action = input("Select the action you want to do (1-9) :")
    if action == "1":
        print("Enter Student Data:")
        firstname = input("Enter First Name \t:")
        lastname = input("Enter Last Name \t:")
        age = int(input("Enter Age \t:"))
        sex = input("Enter Sex \t:")
        major = input("Enter Major \t:")
        student = Student(firstname, lastname, age, sex, major)
        students.append(student)
        print(students)
        for x in students:
            print(x.getFirstName() + " " + x.getLastName() + " " +
                  str(x.getAge()) + " " + x.getSex() + " " + x.getMajor())
    elif action == "2":
        firstname = input("Enter First Name \t:")
        lastname = input("Enter Last Name \t:")
        for x in students:
            if str.lower(x.getFirstName()) == str.lower(firstname) and str.lower(x.getLastName()) == str.lower(lastname):
                print(x.getFirstName() + " " + x.getLastName() + " " +
                      str(x.getAge()) + " " + x.getSex() + " " + x.getMajor())
                print("Name found")

    elif action == "3":
        print("name", "surname", "age", "sex", "major")
        for x in students:
            print(x.getFirstName() + " " + x.getLastName() + " " +
                  str(x.getAge()) + " " + x.getSex() + " " + x.getMajor())

    elif action == "4":
        filtered = []
        minimum = input("Please enter minimum age \t:")
        maximum = input("Please enter maximum age \t:")

        for x in students:
            if int(minimum) < int(x.getAge()) < int(maximum):
                filtered.append(x)
        for y in filtered:
            print(y.getFirstName() + " " + y.getLastName())

    elif action == "5":
        for index, x in enumerate(students):
            print("Student ID: " + str(index) + "Name " + x.getFirstName())
        selected_student = input("Choose a Student \t:")
        selected_student = students[int(selected_student)]
        firstname = input("Enter First Name \t:")
        lastname = input("Enter Last Name \t:")
        age = int(input("Enter Age \t:"))
        sex = input("Enter Sex \t:")
        major = input("Enter Major \t:")
        selected_student.setFirstName(firstname)
        selected_student.setLastName(lastname)
        selected_student.setAge(age)
        selected_student.setSex(sex)
        selected_student.setMajor(major)
        print(selected_student.getFirstName() +
              " Surname" + selected_student.getLastName())
        for x in students:
            print(x.getFirstName() + " " + x.getLastName() + " " +
                  str(x.getAge()) + " " + x.getSex() + " " + x.getMajor())

        print("Student updated.")

    elif action == "6":

        name_delete = input(
            "Enter the name of the student you want to delete. \t:")
        surname_delete = input(
            "Enter the surname of the student you want to delete. \t:")
        found_student_id = 0
        for index, x in enumerate(students):
            if str.lower(x.getFirstName()) == str.lower(name_delete) and str.lower(x.getLastName()) == str.lower(surname_delete):
                print(x.getFirstName() + " " + x.getLastName() + " " +
                      str(x.getAge()) + " " + x.getSex() + " " + x.getMajor())
                print('Name Found.')
                found_student_id = index
        print(found_student_id)
        students.pop(found_student_id)
        for x in students:
            print(x.getFirstName() + " " + x.getLastName() + " " +
                  str(x.getAge()) + " " + x.getSex() + " " + x.getMajor())

    elif action == "7":
        name = input("Enter the name of file. Sample: data.json \t:")

        with open(name, 'w', encoding='utf-8') as f:
            f.write(json.dumps(students, default=vars))

    elif action == "8":
        name = input("Enter the name of file. Sample: studentlist.txt \t:")

        students = []
        f = open(name, "r")
        for x in f:
            x = x.split()
            firstname = x[0]
            lastname = x[1]
            age = x[2]
            sex = x[3]
            major = x[4]
            stud = Student(firstname, lastname, age, sex, major)
            students.append(stud)
        for x in students:
            print(x.getFirstName() + " " + x.getLastName() + " " +
                  str(x.getAge()) + " " + x.getSex() + " " + x.getMajor())

    elif action == "9":
        print("Exiting the program. Please wait...")
        exit()
    else:
        print("Please enter a valid command. (1-9)")
        continue
