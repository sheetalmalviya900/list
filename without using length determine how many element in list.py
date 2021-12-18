name=input("enter the name : ")
i=0
count=0
while(i<len(name)):
    if(name[i]>="a" and name[i]<="z"):
        count+=1
    i+=1
print("Total alphabet in name is :",count)