a,b=input("enter two values two find greatest divisor : ").split(",")
a=int(a)
b=int(b)
c=0
for i in range(1,(a+b)//2):
    if a%i==0 and b%i==0:
        c=i
print("Greatest divisor is ",c)