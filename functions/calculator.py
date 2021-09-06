def add():
    num1 = int(input('enter the num'))
    num2=int(input('enter the num'))
    res=num1+num2
    print('result',res)
def sub():
    num1 = int(input('enter the num'))
    num2 = int(input('enter the num'))
    res = num1 - num2
    print('result', res)
def mul():
    num1 = int(input('enter the num'))
    num2 = int(input('enter the num'))
    res = num1 * num2
    print('result', res)
def div():
    num1 = int(input('enter the num'))
    num2 = int(input('enter the num'))
    res = num1 /num2
    print('result', res)


print('enter the operation')
print('1.addition')
print('2.substraction')
print('3.multilication')
print('4.division')
while True:
  choice=(int(input('enter the choice')))
  if choice==1:
    add()
  elif choice==2:
    sub()
  elif choice==3:
    mul()
  elif choice==4:
    div()
  else:
    print('invalid')