#n='abbc'
#b=n[::-1]
#print(b)

n=input('enter the string')
reverse=n[::-1]
if n==reverse:
  print('palindrome',reverse)
else:
 print('not palindrome',reverse)