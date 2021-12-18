number=input("Enter the number :")
i=0
while(i<len(number)):
    k=len(number)-(i+1)
    num=int(number[i])*(10**k)
    print(num,"+",end="")
    i+=1


    