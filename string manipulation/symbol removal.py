punctuations=',./;:?"}{[]@!#$%^&*()'
string=input('enter the string')
nopunctuation=''
for i in string:
    if i not in punctuations:
        nopunctuation=nopunctuation+i
print(nopunctuation)