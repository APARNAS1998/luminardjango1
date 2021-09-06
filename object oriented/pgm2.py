class Person:
    def setvalue(self,name,age):
        self.name=name #instance variables
        self.age=age
    def printvalue(self):
        print('name',self.name)
        print('age',self.age)
pe=Person()
pe.setvalue('anu',26)
pe.printvalue()