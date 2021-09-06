#start with uppercase letter
#numbers,lowercase,symbols
import re
n=input('enter the string to be checked')
x=(^[A-Z][a-z\d\w]*)$
match=re.fullmatch(x,n)
if match is not None:
    print('valid')
else:
    print('invalid')