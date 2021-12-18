list=[1,2,3,2,4,65,7,6,4,65,2]
i=0
l=[]
while(i<len(list)):
    j=0
    count=0
    while(j<len(list)):
        if(list[i]==list[j]):
            count+=1
        j+=1
    if count==1:
        l.append(list[i])
    i+=1
print(l)