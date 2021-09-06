import re
x="[^abc]"#except a/b or c
matcher=re.finditer(x,'abc#4ab%2c')
for match in matcher:
    print(match.start())
    print(match.group())