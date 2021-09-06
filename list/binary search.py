list=[1,2,3,6,7,8,91,11,13,4,77,88,90]

def binarysearch():
    list.sort()
    print(list)
    ele=int(input('enter the element to be searched'))
    flag=0
    low=0
    upper=len(list)-1
    while low<=upper:
          mid=low+upper//2
          if ele > list[mid]:
              low=mid+1
          elif ele < list[mid]:
              upper=mid-1
          elif ele==list[mid]:
               flag=1
          break
    if flag==1:
        print('found')
    else:
        print('not found')
binarysearch()
