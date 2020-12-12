a = int(input("enter a five digit no : "))
b = int(input("enter single digit no search its presence in a given 5 digit no : "))
n=a
flag=0
while n!=0:
    r=n%10
    n=n//10
    if r==b:
        flag+=1
if flag!=0:
    print("element found ",flag," times")