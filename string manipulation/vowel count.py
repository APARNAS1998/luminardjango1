vowels='aeiou'
string=input('enter the string')
count=0
for i in vowels:
    if i in string:
        count+=1
print(count)
