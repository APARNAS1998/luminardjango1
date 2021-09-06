class Vehicle:
    def modelname1(self,modelname):
        self.modelname=modelname
    def Regnumber(self,Regno):
        self.Regno=Regno
class Bus(Vehicle):
    def colourname(self,colour):
        self.colour=colour
    def printval(self):
        print(self.Regno,self.modelname,self.colour)
B=Bus()
B.modelname1('KSRTC')
B.Regnumber('KL45')
B.colourname('RED')
B.printval()