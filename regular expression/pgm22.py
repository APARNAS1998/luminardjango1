import re
num=(input('enter the pattern for checking'))
x='[a-zA-z]+\d$'#evde plus kodutekkuna kond oru combination elum venam alphabets groupinte ennale valid skull,sllel
#star arunnel onnumillelum valid ennu print cheytene because *considerr cheyyum even there is zero match
match=re.fullmatch(x,num)
if match is not None:
    print('valid')
else:
    print('invalid')
