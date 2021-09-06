#types of variables
#instance variable-related to methods
#static variable=reelated to class acess using class


class School:
    subject='English'#static variable
    def Setvalue(self, name, rollno, mark):
        self.name = name#instance variable
        self.rollno = rollno
        self.mark = mark

    def printvalue(self):
        print(self.name)
        print(self.rollno)
        print(self.mark)
        print(School.subject)


s = School()
s.Setvalue('anu', 22,34)
s.printvalue()
m = School()
m.Setvalue('mickey', 23,76)
m.printvalue()

