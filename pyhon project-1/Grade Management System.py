from zipfile import sizeEndCentDir

student_grades = {}

#add new student

def add_student(name,grade):
    student_grades[name]=grade
    print(f"add{name} with a {grade}")

#Uodate a student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        #rishat = 200
        print(f"{name} with mark updated {grade}")
    else:
        print(f"{name} is not found")

#deleting a student
def delete_student(name):
     if name in student_grades:
        del student_grades[name]
        print(f"{name} has been delete successfully")
     else:
         print(f"{name} is not found")

#view all student
def display_student():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("no student found")
