count={}
f1=open('dict','r')
for line in f1:
    wr=line.split(' ')
    #print(wr)
    for word in wr:
        if word not in count:
            count.update({word:1})
        else:
            val=count[word]
            val+=1
            count.update({word:val})
print(count)