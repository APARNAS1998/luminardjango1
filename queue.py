que=[]
size=int(input('enter the size:'))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que
    if rear>=size:
        print('queue is full')
    else:
        p=int(input('enter the element to insert::'))
        que.insert(rear,p)
        #insert(position,element)
        rear+=1

        for i in range(front,rear):
            print(que[i])
def delete():
    global front,rear,size,que
    if rear==front:
        print('queue is empty')
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])
while n!=1:
    print("enter operation to perform")
    opt=int(input('press 1.enqueue\n 2.dequeue \n '))
    if opt==1:
        insert()
    if opt==2:
        delete()

