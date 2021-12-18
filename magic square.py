magic_square=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while(j<len(magic_square[i])):
        sum=sum+magic_square[i][j]
        j=j+1
    i+=1
print(sum)

i=0
while(i<len(magic_square)):
    j=0
    sum1=0
    while(j<len(magic_square[i])):
        sum1=sum1+magic_square[j][i]
        j+=1
    i+=1
print(sum1)

c=0
d=c
sum2=0
while(c<len(magic_square)):
    sum2=sum2+magic_square[c][d]
    c+=1
print(sum2)
if(sum==sum1==sum2):
    print("")