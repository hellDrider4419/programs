a,b=input("Enter two values to find the gcd of two integer numbers : ").split(",")
a=int(a)
b=int(b)
n=1
if a>b:
    n=a
else:
    n=b
for i in range(1,n):
    if a % i == 0:
        if b % i == 0:
            r = i
print("the greatest common divisor of the given two number is ",r)