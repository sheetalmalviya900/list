string=input("Enter the string:")
reverse_string=string[::-1]
if(string==reverse_string):
    print(string,"is palindrom")
else:
    print(string,"is not palindrom")