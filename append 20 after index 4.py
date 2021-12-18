list=[1,3,5,7,9,11,0,2,4,6,8,10,8,9,0,4,3,0]
i=1
l=[]
while(i<len(list)):
    if(i%5==0):
        l.append(20)
    else:
        l.append(list[i])
    i+=1
print(l)
        