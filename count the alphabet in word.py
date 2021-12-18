name="mississippi"
# name=input("Enter the number:")
i=0
while(i<len(name)):
    count=0
    j=0
    while(j<len(name)):
        if(name[i] == name[j]):
            count+=1
        j+=1
    print( name[i],count)
    i+=1
 