k=["sheetal",1,2.3,88,9,9.0,"mall", True]
i=0
count=0
while(i<len(k)):
    a=type(k[i])
    if(a is int):
        count+=1
    i+=1
print("total boolean in list is:",count)
    # i+=1