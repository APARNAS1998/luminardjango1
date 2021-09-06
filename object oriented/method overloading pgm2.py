class School:
    def admission(self,name,adress):
        self.name=name
        self.adress=adress
        print(self.name,self.adress)
class College(School):
    def admission(self,name,adress,admnno):
        self.name=name
        self.adress=adress
        self.admnno=admnno
        print(self.name,self.adress,self.admnno)
cc=College()
cc.admission('aliya','mumbai',23)
