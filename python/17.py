from array import *

arr= array('i',[])
print("enter 4 values into array")
count=0
for i in range(4):
    arr.append(int(input("")))
    if arr[i]%2==0:
        count+=1
print("number of even values into the array are ",count)