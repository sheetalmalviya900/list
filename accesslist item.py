# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# # Print the last item of the list:
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# Return the third, fourth, and fifth item:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# # This example returns the items from the beginning to, but NOT including, "kiwi":
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# # This example returns the items from "cherry" to the end:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# # This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# # Check if "apple" is present in the list:
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # newlist = [x for x in fruits if "a" in x]
# i=0
# newlist=[]
# while(i<len(fruits)):
#     if("a" in fruits[i]):
#         newlist.append(fruits[i])
#     i+=1
# print(newlist)


a=["rupa","sheetal"]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j=j+1
    i=i+1
print(b)