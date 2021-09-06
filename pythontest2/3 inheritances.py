class Person:
    def employee(self,name,age):
        self.name=name
        self.age=age
class student:
    def Scooldetails(self,studname,studadress):
        self.studname=studname
        self.studadress=studadress
class school(Person):
    def Scooldetails(self,schoolname,adress):
        self.Schoolname=schoolname
        self.adress=adress
class Place(student,school):
    def placedetails(self,place):
        self.place=place
        print(self.name)
        print(self.age)
        print(self.Schoolname)
        print(self.adress)
        print(self.place)
