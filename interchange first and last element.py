num=[12, 35, 9, 56, 24]
i=0
tem=num[0]
num[0]=num[-1]
num[-1]=tem
print(num)