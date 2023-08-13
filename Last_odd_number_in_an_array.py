n=int(input())
l=[]
arr=list(map(int,input().split()))
for i in range(n):
    if arr[i]%2!=0:
        l.append(arr[i])
print(l[-1])