#initialize instance variable
class Person:
    def __init__(self,name,age,address):#constructor
        self.name=name
        self.age=age
        self.address=address

    def printval(self):
        print(self.name)
        print(self.age)
        print(self.address)
obj=Person('anu','25','abc')
obj.printval()
