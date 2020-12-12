n=input("enter a no upto which you want to find the series : ")
sum=0
a=1
l=len(n)
for i in range(1,l+1):
    sum+=a
    if i==l:
        print(a,"=",end="")
    else:
        print(a,"+",end="")
    a=a*10+1
print(sum)