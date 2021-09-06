method overriding...same method name different no of parameters
class Person:
    def printval(self,name):
        self.name=name
        print('inside person method',self.name)
class Child(Person):
    def printval(self,class1):
        self.class1=class1
        print('inside child method',self.class1)
ch=Child()
ch.printval('abc')
#latest method got printed
#child class method printed which means child class ovverrides person class
#ie,child class method overrides parent class method