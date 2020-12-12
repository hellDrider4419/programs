a,b =input("enter a number and its power to calculate the value : ").split(" ")
a=int(a)
b=int(b)
c=1
for i in range(b):
    c*=a
print(" value of ",a," raised to the power ",b," is ",c)