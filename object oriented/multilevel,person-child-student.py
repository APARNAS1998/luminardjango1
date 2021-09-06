class Person:
    def persondata(self,name,ID):
        self.name=name
        self.ID=ID
        print(self.name,self.ID)
class Child(Person):
    def childdata(self,name,parentname):
        self.name=name
        self.parentname=parentname
        print(self.name,self.parentname)
class Student(Child):
    def studentdata(self,rollno,div):
       self.rollno=rollno
       self.div=div
s=Student()
s.studentdata(23,'A')
s.childdata('aparna','santhosh')
s.persondata('santhosh',987)
