n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
   if i%2!=0:
       if i not in s:
           s.append(i)
print(len(s))
