#single inheritance
class Person:   #base class/parent class/super class
    def walk(self):
        print('person is walking')
    def  read(self):
        print('person is reading')
class student(Person):#derived class/sub class/child class
        def exam(self):
            print('student attending the exam')
pe=Person()
pe.walk()
pe.read()
st=student()
st.exam()
st.walk()
st.read()