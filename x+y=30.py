a=[10,11,12,13,14,16,17,18,19,20]
i=0
while(i<len(a)):
    b=i
    while(b<len(a)):
        if(a[i]+a[b]==30):
             print([a[i] ,a[b]])
        b+=1
    i+=1