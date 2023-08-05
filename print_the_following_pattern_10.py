n=int(input())
k=0
s=(n-1)
j=0
for x in range(1,n+1):
    for y in range(0,s):
        print(" ",end="")
    for z in range(k,-1,-1):
        print(z,end="")
    for i in range(1,1+j):
        print(i,end="")
    print()
    s-=1
    j+=1
    k+=1