p=[]
a=int(input("Enter a range to find the armstrong  number "))

for i in range(1,a):
    n=i
    sum=0
    while n!=0:
        r=n%10
        n=n//10
        sum+=r*r*r
    if sum==i:
        p.append(i)
print("armstrong numbers are ",p)