#taking input stsing and setting variables
print("enter a string to print in fibonacci pattern according to the word count\n")
a=input()
x,y=0,1
a=a.split(" ")
l=len(a)
index=1
flag=0


print(" \n" + a[0] + "\n")                              
while flag==0:                              #loop to implement fibonacci series and to print text
    temp=x
    x=y
    y=temp+y
                                                        
    for index in range(index,index+y):         #printing string words on console
        if index==l:
            flag=1
            break
        else:
            print(a[index],end=" ")
    index=index+1
    print("\n")
        
        
