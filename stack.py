stk=[]
size=int(input('enter the size'))
top=0
n=0
def push():
    global top,size
    if(top>size):
        print('stack is full')
    else:
        p=int(input('enter the element want to push'))
        stk.append(p)
        top+=1
def pop():
    global top,size
    if(top<=0):
        print('stack is empty')
    else:
        stk.pop()
        top-=1
def display():
    print(stk)
while (n!=1):
    print('enter the operation to perform')
    print('1.push')
    print('2.pop')
    print('3.display')
while(n!=1):
    print('enter the operation to perform')
    option=int(input('press 1.push 2.pop 3.display')
        if(option==2):
        pop()
        elif(option==3):
        display()

