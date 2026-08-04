from os import access


#Abtractionis hiding implementation details and showing essential feature for user
class car:
    def __init__(self):
        self.acc= False
        self.brk= False
        self.clutch=False
    def start(self):
        self.acc=True
        self.brk=True
        self.clutch=True
    print("car started")
car =car()
car.start()
