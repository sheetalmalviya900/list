elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count1=0
count2=0
even=0
odd=0
while(i<len(elements)):
    if(elements[i]%2==0):
        even+=elements[i]
        count1+=1
    else:
        odd+=elements[i]
        count2+=1
    i+=1
    
print("total even number :",count1) 

print("sum of even number:",even)

print("total odd number  :",count2)

print("sumof odd number  :",odd)

print("total elements    :",count1+count2)

print("sum of all number :",even+odd)
