binary_number = [1, 0, 1,  0]
i=1
sum=0
while(i<=len(binary_number)):
    num=((2**(i-1))*binary_number[-i])
    sum+=num
    i+=1
print(sum)