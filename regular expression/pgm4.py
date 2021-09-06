import re
x='[a-zA-Z]'
matcher=re.finditer(x,'abc$%e&*TASD3asd')
for match in matcher:
    print(match.start())
    print(match.group())