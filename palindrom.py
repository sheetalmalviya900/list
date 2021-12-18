name=[ 'n', 'i', 't', 'i', 'n' ]
list1=[]
i=len(name)-1
while(i>=0):
    list1.append(name[i])
    i-=1
if(name==list1):
    print(name,"palindrom")
else:
    print(name,"not a palindrom")
    # i-=1