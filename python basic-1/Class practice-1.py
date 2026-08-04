# student name and 3 sub marks using constructor and creat method calculate avg

class student:

    def __init__(self,name, mark):
             self.name=name
             self.mark= mark
    def get_avg(self):
        sum = 0
        for val in self.mark:
            sum+=val

        print("hi",self.name,"your avg score is: ",sum/3)


s1=student("Rishat",[70,75,80])
s1.get_avg()