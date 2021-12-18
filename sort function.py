# descending by sort function in list
a=[5,6,3,4,7,8,2,4,9]
i=0
while(i<len(a)):
    j=0
    while(j<len(a)):
        if a[i]<a[j]:
            tem=a[i]
            a[i]=a[j]
            a[j]=tem
        j+=1
    i+=1
print(a)