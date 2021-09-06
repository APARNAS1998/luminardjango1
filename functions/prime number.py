#prime numbers-2,3,5,7
while True:
 num=int(input('enter the num'))
 flag=0

 if num>1:
   for i in range (2,num):
       if num%i==0:
           break
   else:
       flag=1

 if flag==0:
    print('not prime',num)
 else:
   print('prime',num)
