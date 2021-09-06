import re
x='$a'
r='aaa abc aaaaa cgg'#check ending with a
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())