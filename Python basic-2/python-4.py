"""
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")"""

"""
marks = int(input("enter your mark: "))

if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade is B")
elif marks>=60:
    print("grade is C")
else:
    print("Grade D")"""

#nested if/else
username = input("enter your name: ")
password = input("enter your password")

if password =="1234":
    if username == "Admin":
        print("login successfull")
    else:
        print("username")
else:
    print("incorrect username")

