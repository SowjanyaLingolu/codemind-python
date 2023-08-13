n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
b=a.index(k)
for i in range(n):
   if b>=i:
       s+=a[i]
   else:
       break
print(s)
