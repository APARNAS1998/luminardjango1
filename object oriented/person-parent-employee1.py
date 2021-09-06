class Person:
    def setpersonval(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Parent:
    def setparentval(self,name,phnno):
        self.name=name
        self.phnno=phnno
        print(self.name,self.phnno)
class Employee(Person,Parent):
    def setemployeeval(self,name,ID,locn):
        self.name=name
        self.ID=ID
        self.locn=locn
        print(self.name,self.ID,self.locn)
p=Employee()
p.setpersonval('aliya',22,'bollywood')
p.setparentval('mahesh',978)
p.setemployeeval('karan',345,'mumbai')