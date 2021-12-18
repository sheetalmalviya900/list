lst = [15, 6, 7, 10, 12, 20, 10, 28,15,10]
i=0
a=[]
while(i<len(lst)):
    if lst[i] not in a:
        a.append(lst[i])
    i+=1
print(a)