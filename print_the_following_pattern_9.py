n=int(input())
k=1
for x in range(1,n+1):
    for y in range(n-x,0,-1):
        print(" ",end="")
    for z in range(0,k):
        print(x,end="")
    print()
    k+=2