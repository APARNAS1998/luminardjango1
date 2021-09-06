#starting with a and ending with b
import re
n=input('enter the string to be checked')
x='^a[a-zA-Z0-9\w]*b$'
match=re.match(x,n)
if match is not None:
    print('valid')
else:
    print('invalid')