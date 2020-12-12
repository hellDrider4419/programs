n = int(input("enter a five digit no : "))
sum=0
while n!=0:
    r=n%10
    n=n//10
    sum+=r
print("sum of ",n," is ",sum)