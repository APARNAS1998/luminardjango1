import re
x='[a-z]'
matcher=re.finditer(x,'abc$%e&*T3asd')
for match in matcher:
    print(match.start())
    print(match.group())