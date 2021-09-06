s1={1,2,3,4,5,6,78,33,23,44,67}
odd=set()
even=set()
for i in s1:
    if i%2==0:
       even.add(i)
    else:
        odd.add(i)
print(even)
print(odd)