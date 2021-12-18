question_list = [
    "How many continents are there?",           
    "What is the capital of India?",           
    "NG mei kaun se course padhaya jaata hai?"    
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "delhi"],
    #third question ke liye options
    ["software engineering", "Counseling", "Tourism", "Agriculture"]
]

solution_list = [3, 4, 1]

lyfline_option = [
    ["nine","seven"],
    ["bhopal","delhi"],
    ["software engineering","counseling"]
]
solve=[2, 2, 1]

i=0
count=0
while(i<len(question_list)):
    print(question_list[i])
    j=0
    while(j<=len(options_list)):
        print(j+1,options_list[i][j])
        j+=1
    lifeline=input('do you want lifeline:')
    if(lifeline=="yes"):
        if(count<1):
            print("now you have two option")
            s=0
            while(s<len(lyfline_option[i])):
                v=lyfline_option[i][s]
                s+=1
                print(s,v)
            answer1=int(input("enter your answer:"))
            if(answer1==solve[i]):
                print("your answer is correct")
            else:
                print("your answer is wrong")
                print("your life line is finished")
            count+=1
        else:
            print("life line is completed")

    else:
        print("choose your answer by yourself")
        answer=int(input("ENTER YOUR ANSWER"))
        if(answer==solution_list[i]):
            print("WOW YOUR ANSWER IS CORRECT")
        else:
            print("SORRY YOUR ANSWER IS INCORRECT")
            break;
    i+=1