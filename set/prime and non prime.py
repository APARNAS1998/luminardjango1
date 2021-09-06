s1={1,2,3,4,5,66,11,83,76}
prime=set()
nonprime=set()
for i in  s1:
    if i>1:
       for j in range(2,i):
          if i%j==0:
           nonprime.add(i)
           break
          else:
             prime.add(i)
print(prime)
print(nonprime)
