n=int(input())
s=[]
x=0
while(n):
    r=n%10
    if r in s:
        print("Not Unique Number")
        x=1
        break
    else:
        s.append(r)
    n=n//10
if x==0:
    print("Unique Number")
    