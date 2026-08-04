class car:

    def __init__(self,type):
        self.type = type
    def start(self):
        print("car started")
    def stop(self):
        print("car stop")
class Toyotacar(car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

car1=Toyotacar("prius","electric")
print(car1.type)
print(car1.name)
print(car1.start())