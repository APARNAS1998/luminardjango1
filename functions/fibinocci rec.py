#recursion

def recursivefib(n):
   if n<=1:
       return 1
   else:
       recursivefib(n-1) + recursivefib(n-2)
n=10
for i in range(n):
    print(recursivefib(n))
