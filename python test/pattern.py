a=int(input('initial range'))
b=int(input('final range'))
r=5
for i in range(a,b):
    if(i%2==0):
        print(i)
        for k in rang(r,0,-1):
            for j in range(0,k):
                print(i,end='')

            print('\r')
    else:
        for l in range(r):
            for m in range(0,l+1):
                print(i,end='')
            for