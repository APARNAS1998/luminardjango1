#functions with arguments and return types
def fact(num):
    sum = 1
    if num > 0:
        for i in range(1, num + 1):
            sum= sum* i
        return (sum)
    elif num==0:
        return('Factorial is 1')
    else:
        return('invalid')



print(fact(-1))

