number = [50, 40, 23, 70, 12, 5, 10,78,7,56]
i=0
min=number[i]
scnd_min=number[i]
while(i<len(number)):
    if(number[i]<min):
        scnd_min=min
        min=number[i]
    elif(number[i]<scnd_min):
        scnd_min=number[i]
    i+=1
print(scnd_min)