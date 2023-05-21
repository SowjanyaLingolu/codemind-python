def lcm(a,b):
    for i in range(1,a+1):
        for j in range(1,b+1):
            if a%i==0 and b%i==0:
                g=i
    I=(a*b)/g
    print(int(I))
a,b=map(int,input().split())
lcm(a,b)