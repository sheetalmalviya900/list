a=[]
for i in range(3):
    b=[]
    for j in range(5):
        j=int(input("enter the number"))
        b.append(j)
    a.append(b)
print("THE NUMBERS OCCUR IN THREE YEARS")
count=0
s=[]
for i in range(3):
    for j in range (5):
        k=a[i][j]
        count+=k
        # s.append(k)
        print(a[i][j],end=",")
    print()
print("total mark occur in last three year",count)