list=['1','2','3','4','5','6','7','8','9']
i=1
l=[]
while(i<len(list)):
    l.append(list[i-1]+list[i])
    i+=2
print(l)

