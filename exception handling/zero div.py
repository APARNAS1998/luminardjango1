num1=int(input('enter the first number'))
num2=int(input('enter the second number'))
try:
    res=num1/num2
    print(res)
except Exception as e:
    print(e.args)