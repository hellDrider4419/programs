a= int(input("Enter a number to find its divisor : "))
print(" all divisor of ",a," are ",end="")
for i in range(1,a//2+1):
    if a%i==0:
        print(i,end=" ")
