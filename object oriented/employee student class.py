class Employee:
    def name(self,name):
        self.name=name
    def ID(self,ID):
        self.ID=ID
    def time(self,worktime):
        self.worktime=worktime
class Student(Employee):
    def work(self,time):
        self.time=time
        print(name,ID,time)
s1=Student()
s1.ID(2301)
