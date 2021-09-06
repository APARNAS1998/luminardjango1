class Vehicle:
    def __init__(self,model,regno,colour):
        self.model=model
        self.regno=regno
        self.colour=colour
    def print(self):
        print(self.model)
        print(self.regno)
        print(self.colour)
    def __str__(self):
        return self.model+self.colour
v=Vehicle('ktm','kl23','black')
v.print()
print(v)