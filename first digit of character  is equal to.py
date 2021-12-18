list=[1234,122,1984,39372,100]
i=0
l=[]
while(i<len(list)):
    k=list[i]
    s=str(k)
    first=s[0]
    l.append(first)
    i+=1
a=0
while(a<len(l)):
    value=l[0]==l[a]
    if(value==False):
        break;
    a+=1
print("output is",value)