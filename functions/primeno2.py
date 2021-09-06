n=int(input('enter the number'))
flag = 0
for i in range(2,n):
    if n%i==0:
        flag==0
        break
    else:
        flag==1
if flag==1:
    print(i)
else:
    print('invalid')