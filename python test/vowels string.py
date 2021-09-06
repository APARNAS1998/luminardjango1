string=input('enter the string')
vow='aeiou'
empty=''
for i in string:
   if i not in vow:
     empty=empty+i
print(empty)

