class employee:

    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showdetails(self):

        print("role=",self.role)
        print("dept=",self.role)
        print("salary=",self.salary)

class Engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=name
        super().__init__("Engr","IT","750000")

e1 = Engineer("Rishat","21")
e1.showdetails()