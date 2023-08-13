n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(n):
    sum+=a[i]
avg=sum//n
s=[]
for i in range(n):
    if a[i]<=avg:
        s.append(a[i])
print(len(s))
