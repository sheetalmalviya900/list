list1 = [12, -7, 5, 64, -14]
i=0
positive=0
negative=0
while(i<len(list1)):
    if(list1[i]>0):
        positive+=1
    else:
        negative+=1
    i+=1
print("positive number is",positive)
print("negative number is",negative)