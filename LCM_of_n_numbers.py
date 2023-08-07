import math
def I(a):
    lcm=a[0]
    for i in range(1,len(a)):
        lcm=lcm*a[i]//math.gcd(lcm,a[i])
    return lcm
n=int(input())
a=list(map(int,input().split()))
b=I(a)
print(b)
