min=int(input('enter the number'))
max=int(input('enter the number'))
for a in range(min,max+1):
    if(a>1):
      for i in range(2,a):
        if(a%i==0):
            break
      else:
        print(a)