n=int(input())
a=list(map(int,input().split()))
s1=[]
s2=[]
for i in a:
    if i%2==0:
        s1.append(i)
    else:
        s2.append(i)
print(*(s2+s1))