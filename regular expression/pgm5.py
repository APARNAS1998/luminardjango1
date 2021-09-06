import re
x='[0-9]'
matcher=re.finditer(x,'ab c$%e&*TASD3asd')
for match in matcher:
    print(match.start())
    print(match.group())