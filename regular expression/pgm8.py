import re
x='\d'#all digits
matcher=re.finditer(x,'abc$%e&*TA SD3a*sd')
for match in matcher:
    print(match.start())
    print(match.group())