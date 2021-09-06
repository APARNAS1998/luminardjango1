class Teacher:
    def __init__(self,name,ID,Dep):
        self.name=name
        self.ID=ID
        self.Dep=Dep
    def print(self):
        print(self.name,self.ID,self.Dep)
Teach=Teacher('revathy',221,'zoology')
Teach.print()