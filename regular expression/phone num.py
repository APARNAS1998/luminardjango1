import re
num=(input('enter the phone number'))
x='[+][9][1]\d{10}$'
match=re.fullmatch(x,num)
if match is not None:
    print('valid')
else:
    print('invalid')
