a=["zero","one","two","three","four","five","six","seven","eight","nine"]
number=input("Enter the number :-")
i=0
while(i<len(number)):
    k=int(number[i])
    print(a[k],end=" ")
    i+=1
print()