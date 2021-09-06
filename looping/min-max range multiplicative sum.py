#printing even numbers in a range using while loop

min=int(input('enter the lower range'))
max=int(input('enter the higher range'))
while min<=max:
   if(min%2==0):
     print(min)
   min+=1

