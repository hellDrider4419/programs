p=[]
a=int(input("Enter a range to find the pallandrome number "))

for i in range(1,a):
    n=i
    rev=0
    while n!=0:
        r=n%10
        n=n//10
        rev=rev*10+r
    if rev==i:
        p.append(i)
sp=[]
for i in p:
    j=i*i
    n=j
    rev=0
    while n!=0:
        r=n%10
        n=n//10
        rev=rev*10+r
    if rev==j:
        sp.append(i)
print("Super pallandrome are ",sp)