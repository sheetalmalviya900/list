a=[[1,3],[8,9,5,],4,6,[1,4,6,8,9],8,9]
sum=0
for i in a:
    n=i
    if (type(n) is list):
        for j in n:
            sum+=j
    else:
        sum+=i
print(sum)
