a,b,c,d=input("Enter four integer values : ").split(",")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
minimum=0

if a <= b and a <= c and a <= d:
    minimum = a
    x = b
    y = c
    z = d
elif b<=a and b<=c and b<=d:
    minimum=b
    x = a
    y = c
    z = d
elif c<=a and c<=b and c<=d:
    minimum=c
    x = b
    y = a
    z = d
else:
    minimum=d
    x = b
    y = c
    z = a
if x<=y  and x<=z:
    print(x," is  3rd maximum")
elif y<=x and y<=z:
    print(y," is 3rd maximum")
else:
    print(z," is 3rd maximum")