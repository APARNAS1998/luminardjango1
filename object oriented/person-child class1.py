#multiple inheritance
class Person:
    def set(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Child:
    def setvalue(self,school,std):
        self.school=school
        self.std=std
        print(self.school,self.std)
class Student(Person,Child):
    def printvalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
st=Student()
st.set('anu',22,'greenvilla')
st.setvalue('luminar',2)
st.printvalue(22,98)