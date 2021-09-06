class School:
     def Setvalue(self,name,rollno,subject,mark):
        self.name=name
        self.rollno=rollno
        self.subject=subject
        self.mark=mark
     def printvalue(self):
         print(self.name)
         print(self.rollno)
         print(self.subject)
         print(self.mark)
s=School()
s.Setvalue('anu',22,'Eng',34)
s.printvalue()
