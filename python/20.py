a=int(input("Enter a four digit no to find its reverse and print it in word form : "))
b=["zero","one","two","three","four","five","six","seven","eight","nine"]
rev=0
c=a
words=""
while c!=0:
    r=c%10
    c=c//10
    rev=rev*10+r
    words=words + " " + b[r]
print("reverse is ",rev," and in words form " + words)

