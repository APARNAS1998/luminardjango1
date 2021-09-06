class Person:
    def personval(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Parent:
    def parentval(self,name,phnno,adrs):
        self.name=name
        self.phnno=phnno
        self.adrs=adrs
        print(self.name,self.phnno,self.adrs)
class Student(Person,Parent):
    def studentval(self,name,school):
        self.name=name
        self.school=school
        print(self.name,self.school)
s=Student()
s.personval('betty',18,'Riverdale')
s.parentval('hal',46,'Riverdale')
s.studentval('betty','riverdalehigh')