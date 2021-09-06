#minimum length 8 maximum 15 no numbers
import re
n=input('enter the string to be checked')
x='[\D]{8,15}'
match=re.match(x,n)
if match is not None:
    print('valid')
else:
    print('invalid')