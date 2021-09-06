class Employee:
       def __init__(self,name,ID,salary):
           self.name=name
           self.ID=ID
           self.salary=salary
       def printval(self):
           print(self.name,self.ID,self.salary)
obj=Employee('aparna',2301,2340000)
obj.printval()

