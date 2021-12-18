# # a=[12,43,5,6,4,7,6,7,6,78,67]
# # b=[2,4,6,8,9,6,7,9,7,8,9,8,8]
# # print(a+b)

# list1 = ["M", "na", "i", "shee"] 
# list2 = ["y", "me", "s", "tal"]
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)


# list1 = ["M", "na", "i", "Ke"] 
# list2 = ["y", "me", "s", "lly"]
# i=0
# k=[]
# while(i<len(list1)):
#     list3=list1[i]+list2[i]
#     k.append(list3)
#     i+=1
# print(k)

# # in different way
# list1=["Hello","take"]
# list2=["Dear","Care"]
# newList=[] 
# for i in list1:
#      for j in list2:
#          newList.append(i+' '+j)
# print(newList)

# list1=["Hello","take"]
# list2=["Dear","Care"]
# newList=[] 
# i=0
# while(i<len(list1)):
#     j=0
#     while(j<len(list2)):
#         newList.append(list1[i]+list2[j])
#         j+=1
#     i+=1
# print(newList)

num=["0",'1','2','3','4']
clr=["red",'green','blue','yellow','black']
hund=['100','200','300','400','500']
i=0
k=[]
while(i<len(num)):
    a=(num[i]+clr[i]+hund[i])
    k.append(a)
    i+=1
print(k)

