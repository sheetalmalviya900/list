numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
index=0
length_list=len(numbers)
num=0
num2=0
while(index<length_list):
    marks=numbers[index]
    if(marks<=40 and marks>=20):
        num+=1
    else:
        num2+=1
    index+=1
print(" Total Number between 20 and 40 is:",str(num))
print("total number out of 20 and 40 is:",str(num2))