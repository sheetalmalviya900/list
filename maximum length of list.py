list1=[1,[2],1,[4,6],9,2,[4,3,6,9]]
max=0
for i in list1:
    if type(i)==list:
       if len(i)>max:
        max=len(i)
        m=i
print(max,i)