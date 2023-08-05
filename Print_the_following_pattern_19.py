n=int(input())
k=1
s=(n-1)
j=0
for x in range(1,n+1):
    for y in range(0,s):
        print(" ",end="")
    for z in range(1,1+k):
        print(z,end="")
    for i in range(j,0,-1):
        print(i,end="")
    print()
    s-=1
    j+=1
    k+=1