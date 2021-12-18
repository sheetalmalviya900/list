a=["v","y"]
user=int(input("Enter the number"))
i=0
while(i<user):
    j=0
    while(j<len(a)):
        print(a[j],i,end=" ")
        j+=1
    print()
    i+=1