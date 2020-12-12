n=int(input("enter a no upto which you want to find the series : "))
sum=0
for i in range(1,n+1):
    sum+=i*i
    if i==n:
        print(i*i,"=",end="")
    else:
        print(i*i,"+",end="")
print(sum)