a=int(input("enter a number to find the factorial : "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print("Factorial of ",a," is ",fact)