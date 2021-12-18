number = [50, 40, 23, 70, 12, 5, 10,78,7,56]
i=0
max=number[i]
scnd_mx=number[i]
while i<len(number):
    if(number[i]>max):
        scnd_mx=max
        max=number[i]
    elif(number[i]>scnd_mx):
        scnd_mx=number[i]
    i+=1
print(scnd_mx)