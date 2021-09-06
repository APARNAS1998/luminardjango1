def addition():
    num1=float(input('enter the first number'))
    num2=float(input('enter the second number'))
    res=num1+num2
    print('result=',res)
def substraction():
    num1 = float(input('enter the first number'))
    num2 = float(input('enter the second number'))
    res = num1 - num2
    print('result=',res)
def multiplication():
    num1 = float(input('enter the first number'))
    num2 = float(input('enter the second number'))
    res = num1 * num2
    print('result=',res)
def division():
    num1 = float(input('enter the first number'))
    num2 = float(input('enter the second number'))
    res = num1/num2
    print('result=',res)
def floordivision():
    num1 = float(input('enter the first number'))
    num2 = float(input('enter the second number'))
    res = num1 // num2
    print('result=',res)
def exponent():
    base = float(input('enter the base number'))
    exponent = float(input('enter the exponent number'))
    res = base**exponent
    print('result=',res)

print('enter the operation')
print('1.addition')
print('2.substraction')
print('3.multiplication')
print('4.division')
print('5.floor division')
print('6.exponential')
choice=int(input('choice='))
if choice==1:
    addition()
elif choice==2:
    substraction()
elif choice==3:
   multiplication()
elif choice == 4:
    division()
elif choice == 5:
   floordivision()
elif choice == 6:
    exponent()
else:
    print('invalid')











