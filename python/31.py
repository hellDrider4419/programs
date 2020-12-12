a=int(input("Enter the range to print fabonnaci series : "))
l=[0,1]
new=l[-1] + l[-2]
while not new>a:
    l.append(new)
    new = l[-1] + l[-2]
print("fabonnaci series ",l)