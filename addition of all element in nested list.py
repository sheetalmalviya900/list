list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,4]
for i in list1:
    if(i in list2):
        print("this is present in list :",i)
    else:
        print("this is not present in list :",i)
