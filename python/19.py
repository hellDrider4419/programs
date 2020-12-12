a=int(input("Enter a integer number to find it reverse : "))
b=0
c=a
while c!=0:
    r=c%10
    c=c//10
    b=b*10+r
print("Reverse of ",a," is ",b)