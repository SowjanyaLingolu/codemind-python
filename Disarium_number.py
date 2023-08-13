n=int(input())
length=len(str(n))
Temp=n
summ=0
rem=0
while Temp>0:
    rem=Temp%10
    summ=summ+int(rem**length)
    Temp=Temp//10
    length=length-1
if summ==n:
    print("True")
else:
    print("False")