import re
x='\w'
matcher=re.finditer(x,'abc$%e&*TA SD3a*sd')
for match in matcher:
    print(match.start())
    print(match.group())