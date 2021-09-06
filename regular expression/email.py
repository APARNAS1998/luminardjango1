import re
num=input('enter the email ID')
x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$'
match=re.fullmatch(x,num)
if match is not None:
    print('valid')
else:
    print('invalid')
