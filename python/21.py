a=input("Enter a four digit no to find its reverse and print it in word form : ")
b=["zero","one","two","three","four","five","six","seven","eight","nine"]
b1=["","ten","twenty","thirty","fourty","fifty","sixty","eventy","eighty","ninety"]
rev=0
l=len(a)
a=int(a)
c=a
words=""
while c!=0:
    r=c%10
    c=c//10
    rev=rev*10+r
    if r!=0:
        if l==10:
            words=words + b[r] + " billion "
        elif l==9 or l==6 or l==3:
            words=words + b[r] + " hundred "
        elif l==8 or l==5 or l==2:
            words=words + b1[r] + " "
        elif l==7:
            words=words + b[r] + " million "
        elif l==4:
            words=words + b[r] + " thousand "
        elif l==1:
            words=words + b[r]
    l-=1
print("reverse is ",rev," and in words form " + words)

