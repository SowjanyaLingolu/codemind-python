n=int(input())
a=list(map(int,input().split()))
p=[]
for i in a:
   c=0
   for j in range(1,i+1):
       if i%j==0:
           c+=1
   if c==2:
       p.append(i)
b=sum(p)/len(p)
print(format(b,".2f"))
