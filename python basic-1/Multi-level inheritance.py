class car:

    def start(self):
        print("car stared")
    def stop(self):
        print("car stoped")
class Toyotacar(car):

    def __init__(self,brand):
        self.brand = brand
class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type
car1=Fortuner("diesel")
print(car1.type)
car1.start()
