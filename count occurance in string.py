# a="my name is sheetal"
# i=0
# while(i<len(a)):
#     count=0
#     j=0
#     while(j<len(a)):
#         if(a[i]==a[j]):
#             count+=1
#         j+=1
#     print(a[i],"=",count)
#     i+=1
# # print(count)

a= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
l=[]
while(i<len(a)):
    count=0
    j=0
    while(j<len(a)):
        if(a[i]==a[j]):
            count+=1
            if(a[i] not in l):
                l.append(a[i])
        j+=1
    print(a[i],"=",count)
    i+=1
print(l)
