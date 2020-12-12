n=int(input("enter a no upto which you want to find the series : "))
sum=0
for i in range(1,n+1):
    sum+=i*2
    if i==n:
        print(2*i,"=",end="")
    else:
        print(i*2,"+",end="")
print(sum)