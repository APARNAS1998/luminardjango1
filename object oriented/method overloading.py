#method overloading...same method name,different number of parameters
#python do not support method overloading


class Person:
    def show(self,num1):
        self.num1=num1
        print(self.num1)
class student(Person):
    def show(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1,self.num2)
per=student()
per.show()