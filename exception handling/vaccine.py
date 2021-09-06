age=int(input('enter the age of person'))
if age<18:
    raise Exception ('the person can not be vaccinated')
else:
    print('admitted for  vaccination')