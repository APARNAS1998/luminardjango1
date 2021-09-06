class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
    def num(self,n3):
        self.n3=n3
        print(self.n3)
np=Operators()
np.num(6,4)
#method overloading not happen in python
#latest method runs in python
#same mthod name different number of parameters