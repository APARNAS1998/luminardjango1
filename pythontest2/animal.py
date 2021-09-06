class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Dog(Animal):
    def breedname(self,breed):
        self.breed=breed
        print(self.name)
        print(self.age)
        print(self.breed)
d=Dog('chakki',2)
d.breedname('Beagle')