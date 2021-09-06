lst=[1,3,4,5,6]
#without using lambda function
#def chck_even():

#3    return num%2==0
#evennum=list(filter(chck_even(),lst))
evens=list(filter(lambda num:num%2==0,lst))
print(evens)
odds=list(filter(lambda num:num%2!=0,lst))
print(odds)