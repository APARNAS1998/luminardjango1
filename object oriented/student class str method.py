class Student:
    def __init__(self,name,rollno,department,colleg):
        self.name=name
        self.rollno=rollno
        self.department=department
        self.colleg=colleg
    def print(self):
        print(self.name,self.rollno,self.department,self.colleg)
    def __str__(self):
        return self.name+self.department+str(self.rollno)#return cheyyan str datattypelekk rollno ne convert cheyt
s=Student('aparna','23','computer science','stgits college ')
s.print()
print(s)