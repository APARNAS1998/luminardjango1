#s=set()
#lmt=int(input('enter the limit'))
#for i in range(lmt):
 #   element=int(input('eneter the element'))
#    element2=element*element
#    s.add(element2)
#print(s)
#sets are mutable{we can make chenges in it}
a={1,2,3,4,5,6,7,8,9}
b=set()
for i in a:
    b.add(i**2)
print(b)
