n=int(input())
a=list(map(int,input().split()))
sum=0
m=n-1
for i in a:
    sum+=i*(2**m)
    m-=1
print(sum)
