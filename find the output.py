# geekcode=[1,2,3,4]
# geekcode.append([5,6,7,8])
# print(geekcode)

check1=['learn','quiz','practice','contribute']
check2=check1
check3=check1[:]
check2[0]='code'
check3[1]='mcq'
count=0
for c in (check1,check2,check3):
    if c[0]=='code':
        count+=1
    if c[1]=='mcq':
        count+=10
print(count)

# list1=range(100,110)
# print(list1.index(109))

# list1=[1998,2002]
# list2=[2014,2016]
# print((list1+list2)*2)

# print(list(range(4,30,2)))

# for i in range(4,31):
#     if i%2==0:
#         print(i,end=" ")

# for i in range(4,30):
#     if i%2==0:
#         print(i,end=" ,")