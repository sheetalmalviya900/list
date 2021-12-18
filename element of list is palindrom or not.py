a=["chayya","mom","sheetal","nitin"]
i=0
count1=0
count2=0
while(i<len(a)):
    b=a[i]
    reverse=b[::-1]
    if(a[i]==reverse):
        count1+=1
        print(a[i],"is palindrom")
    else:
        count2+=1
        print(a[i], "is not a palindrom")
    i+=1
print("palindrom",count1)
print("not palindrom",count2)