num=int(input('enter the number'))
fact=1
while num>1:
   for i in range(1,num):
    fact=fact*i
    print(fact)
