n=int(input())
a=n*n
su=0
while a!=0:
    r=a%10
    su=su+r
    a//=10
if su==n:
    print("Neon Number")
else:
    print("Not Neon Number")