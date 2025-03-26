#CMSC3380_Assignment3_GroupNUM.py
import pickle
import os

DATA_FILE = "CMSC3380_Assignment3_Group1.dat"

run = True
courseDictionary = dict()
studentDictionary = dict()

def saveData():
    with open(DATA_FILE, "wb") as c:
        pickle.dump((courseDictionary, studentDictionary), c)
    print("Data saved to file.")

def loadData():
    global courseDictionary, studentDictionary
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as c:
            courseDictionary, studentDictionary = pickle.load(c)
        print("Data loaded from file.")
    else:
        print("No data file found.")

def menu():
    print("-------------------------------\n")
    print("   Student/Course Dictionary   \n")
    print("-------------------------------\n")    
    print("(1) Add a Course")
    print("(2) Delete a Course")
    print("(3) Add a Student")
    print("(4) Delete a Student")
    print("(5) List all Courses")
    print("(6) List all Students")
    print("(7) Add a Course to Student")
    print("(8) Delete a Course from Student")
    print("(9) List Student Courses")
    print("(0) QUIT\n")

def addCourse(courseId, courseName):
    courseDictionary[courseId] = courseName
    print(f"You added course: {courseId} - {courseName}")

def deleteCourse(courseId):
    if courseId in courseDictionary:
        print(f"You deleted: {courseDictionary[courseId]}")
        del courseDictionary[courseId]
    else:
        print("Course ID not found.")

def addStudent(studentId, studentName, studentMajor, studentEmail):
    if studentId not in studentDictionary:
        studentDictionary[studentId] = {
            "Name": studentName,
            "Major": studentMajor,
            "Email": studentEmail,
            "Courses": []
        }
        print(f"Student added: {studentId}, {studentName}")
    else:
        print("Student ID already exists.")

def deleteStudent(studentId):
    if studentId in studentDictionary:
        print(f"You deleted: {studentDictionary[studentId]['Name']}")
        del studentDictionary[studentId]
    else:
        print("Student ID not found.")

def addCourseToStudent(studentId, courseId):
    if studentId in studentDictionary and courseId in courseDictionary:
        if courseId not in studentDictionary[studentId]["Courses"]:
            studentDictionary[studentId]["Courses"].append(courseId)
            print(f"You added {courseDictionary[courseId]} to {studentDictionary[studentId]['Name']}")
        else:
            print(f"{studentDictionary[studentId]['Name']} is already enrolled in {courseDictionary[courseId]}")
    else:
        print("Invalid Student ID or Course ID.")

def deleteCourseFromStudent(studentId, courseId):
    if studentId in studentDictionary:
        if courseId in studentDictionary[studentId]["Courses"]:
            studentDictionary[studentId]["Courses"].remove(courseId)
            print(f"Removed {courseDictionary.get(courseId, courseId)} from {studentDictionary[studentId]['Name']}")
        else:
            print(f"{studentDictionary[studentId]['Name']} is not enrolled in {courseId}")
    else:
        print("Invalid Student ID.")

def listStudentCourses(studentId):
    if studentId in studentDictionary:
        courses = studentDictionary[studentId]["Courses"]
        if not courses:
            print(f"{studentDictionary[studentId]['Name']} is not enrolled in any courses.")
        else:
            print(f"{studentDictionary[studentId]['Name']} is enrolled in:")
            for cid in courses:
                cname = courseDictionary.get(cid, "Unknown Course")
                print(f" - {cid}: {cname}")
    else:
        print("Student ID not found.")

# Load data from file on startup
loadData()

# Main loop
while run:
    menu()
    choice = input("Enter a number for your choice: ")

    if choice == "1":
        courseId = input("Enter the Course ID to add: ")
        courseName = input("Enter the Course Name: ")
        addCourse(courseId, courseName)

    elif choice == "2":
        courseId = input("Enter the Course ID to delete: ")
        deleteCourse(courseId)

    elif choice == "3":
        studentId = input("Enter the Student ID to add: ")
        studentName = input("Enter the Student Name: ")
        studentMajor = input("Enter the Student Major: ")
        studentEmail = input("Enter the Student Email: ")
        addStudent(studentId, studentName, studentMajor, studentEmail)

    elif choice == "4":
        studentId = input("Enter the Student ID to delete: ")
        deleteStudent(studentId)

    elif choice == "5":
        if courseDictionary:
            print("All Courses:")
            for cid, cname in courseDictionary.items():
                print(f" - {cid}: {cname}")
        else:
            print("No courses available.")

    elif choice == "6":
        if studentDictionary:
            print("All Students:")
            for sid, details in studentDictionary.items():
                print(f" - {sid}: {details['Name']}, {details['Major']}, {details['Email']}")
        else:
            print("No students available.")

    elif choice == "7":
        studentId = input("Enter the Student ID to add a course to: ")
        courseId = input("Enter the Course ID to add: ")
        addCourseToStudent(studentId, courseId)

    elif choice == "8":
        studentId = input("Enter the Student ID to remove a course from: ")
        courseId = input("Enter the Course ID to remove: ")
        deleteCourseFromStudent(studentId, courseId)

    elif choice == "9":
        studentId = input("Enter the Student ID to list courses for: ")
        listStudentCourses(studentId)

    elif choice == "0":
        saveData()
        print("Exiting the program. Goodbye!")
        run = False

    else:
        print("Invalid choice. Please enter a number between 0 and 9.")
