#Create objects of the following file and print the details of student with maximum mark? anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,bca,198 maya,5, bba,195
class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printdata(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.mark)
lst=[]
f=('filepgm1','r')
for i in f:
    d=i.rstrip('\n').split(',')
    print(d)
    name=d[0]
    rollno=d[1]
    course=d[2]
    mark=d[3]
    s1=Student(name,rollno,course,mark)
    s1.print(data)
    lst.append(s1)
mark=[]
for st in lst:
    if(st,mark==max(mark)):
        print(st.rollno,st.name,st.course,st.mark)