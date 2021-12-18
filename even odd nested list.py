a=[[11,23],[8,9,5,],4,6,[10,4,67,87,9],8,9]
sum=0
for i in a:
    n=i
    if (type(n) is list):
        for j in n:
            if(j%2==0):
                print(j,"even")
            else:
                print(j,"odd")
    else:
        if(n%2==0):
            print(n,"even")
        else:
            print(n,"odd")
