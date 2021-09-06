a='luminar'
n=input('enter the character to check')
flag=0
for i in a:
    if i in n:
       flag=1
if(flag==1):
    print('present')
else:
       print('not present')
