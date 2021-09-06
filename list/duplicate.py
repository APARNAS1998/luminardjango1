a=[1,2,3,4,5,5,6,7,1,2,3]
lst=[]
for i in a:
    if i not in lst:
        lst.append(i)
    else:
       print(i)
