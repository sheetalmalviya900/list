a=[9,2,5,6,7,8,0,3,]
i=0
n=int(input("enter how many element you want to remove in list"))
b=[]
while(i<len(a)-n):
    b.append(a[i])
    i+=1
print(b)