import math as m
n=int(input("enter a range to find th e prime number : "))
l=[1]
for i in range(2,n):
    flag=0
    for j in range(2,int(m.sqrt(i)+1)):
        if i%j==0:
            flag=1
            break
    if flag==0:
        l.append(i)
print(l)