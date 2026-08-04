
Student = {
    "name":"shakib al-hasan",
    "subject": {
        "phy":80,
        "chem":90,
        "math":40,

    },
    "Dept.": "Software Engineering",
}
print(Student["subject"])

print(list(Student.keys()))
print(len(Student))
print(Student.items())
Student.update({"city":"Dhaka"})
print(Student)
#Adding new dict
New_dict = {"town":"Galachipa"}
Student.update(New_dict)
print(Student)