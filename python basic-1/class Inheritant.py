class car:

    def start(self):
        print("car stared")
    def stop(self):
        print("car stoped")

class Toyotacar(car):

    def __init__(self,name):
        self.name=name

car1=Toyotacar("black")
car2=Toyotacar("white")
print(car1.start())