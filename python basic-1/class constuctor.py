
class student:
    University_name="ABC University"
    name="Anonymous"#class Attribute
  #difining constructor
    def __init__(self,name,mark):
        self.name=name #Object Attribute
        self.mark=mark

    #Method under class
    def welcome(self):
        print("welcome student",self.name)
    def get_mark(self):
        print(self.get_mark)
        #object declaration
s1=student("Rishat",70)
print(s1.name,s1.mark)
s1.welcome()
s1.get_mark()

s2=student("Modon",40)
print(s2.name,s2.mark)
s2.welcome()
print(s1.get_mark())