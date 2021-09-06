class Employee:
    def setvalue(self,name,age,ID):
        self.name=name
        self.age=age
        self.ID=ID
    def printvalue(self):
        print('Employee name:',self.name)
        print('Employee age:',self.age)
        print('Employee ID:',self.ID)
emp1=Employee()
emp1.setvalue('aparna',22,1024)
emp1.printvalue()