print("# # # # # # # # # # # # # # # # # # # # # # #              SIMPLE CALCULATOR               # # # # # # # # # # # # # # # # # # # # # # #")
a,b,c=input("enter an expression to find its output(saperate operators and operands with blank space)\n").split(" ")
a=int(a)
c=int(c)
if b=='+':
    print("performing addition \n",a," " + b + " ",c," = ",a+c)
elif b=='-':
    print("performing subtraction \n",a," " + b + " ",c," = ",a-c)
elif b=='*':
    print("performing multiplication \n",a," " + b + " ",c," = ",a*c)
elif b=='/':
    print("performing division \n",a," " + b +" ",c," = ",a/c)