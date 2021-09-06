class Work():
    def __init__(self,name,rollno,course,marks):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.marks=marks
    def print(self):
        print('name::',self.name)
        print('rollno::',self.rollno)
        print('course::',self.course)
        print('marks::',self.marks)
f1=open('work','r')
for line in f1:
    l=line.split(',')
    name=l[0]
    rollno=l[1]
    course=l[2]
    mark=l[3]
    wo=Work(name,rollno,course,marks)

for line in f1:
    l=line.split(',')
    name=l[0]
    rollno=l[1]
    course=l[2]
    marks=l[3]
    wo=work(name,rollno,course,marks)
    wo.print()
