import re
x='+a'#a including group
a='aaa abc abba aaa bba'
matcher=re.finditer(x,a)
for match in matcher:
    print(match.start())
    print(match.group())