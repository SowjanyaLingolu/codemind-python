n=int(input())
maxx=0
while(n):
    r=n%10
    if r>maxx:
        maxx=r
    n//=10
print(maxx)