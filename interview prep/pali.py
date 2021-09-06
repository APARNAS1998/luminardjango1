n=int(input('num'))
sum=0
while(n>0):
    temp=n
    r=n%10
    sum=sum+r*r*r
    n=n//10
if (temp==sum):
    print('arm')
else:
    print('not')
