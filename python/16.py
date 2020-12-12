a,b,c,d=input("Enter four integer values : ").split(",")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if a>=b  and a>=c and a>=d:
    print(a," is maximum")
elif b>=a and b>=c and b>=d:
    print(b," is maximum")
elif c>=a and c>=b and c>=d:
    print(c," is maximum")
else:
    print(d," is maximum")

if a<=b  and a<=c and a<=d:
    print(a," is minimum")
elif b<=a and b<=c and b<=d:
    print(b," is minimum")
elif c<=a and c<=b and c<=d:
    print(c," is minimum")
else:
    print(d," is minimum")