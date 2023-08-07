n=int(input())
N=n*n
s=0
while(N):
    r=N%10
    s+=r
    N=N//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")