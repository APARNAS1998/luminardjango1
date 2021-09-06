class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print('name::',self.name)
        print('age::',self.age)
    def __str__(self):
        return self.name
