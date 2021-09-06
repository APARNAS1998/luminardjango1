list1=[1,2,3,4,5,6,78,8]

def linearsearch(list1):
     e=input('enter the element to be checked')
     flag=0
     for i in list1:
        if i==e:
             flag=1
             break
     if flag==0:
       print('element not found')
     else:
       print('element found')
linearsearch(list1)