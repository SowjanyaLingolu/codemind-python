n=int(input())
p=1
s=0
while(n):
    r=n%10
    p=p*r
    s=s+r
    n=n//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")