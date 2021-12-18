num=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,27]
i=0
while(i<len(num)):
    a=1
    sum=0
    while(a<=num[i]):
        if(num[i]%a==0):
            sum+=1
        a+=1
    if(sum==2):
        print(num[i],": is prime number")
    else:
        print(num[i],": is composite number")
    i+=1