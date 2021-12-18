fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
i=0
newlist=[]
while(i<len(fruits)):
    if("a" in fruits[i]):
        newlist.append(fruits[i])
    i+=1
print(newlist)