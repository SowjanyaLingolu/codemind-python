a=50
b=60
c=100
d,e,f=map(int,input().split())
if d>a and e>b and f>c:
    print("10")
elif d>a and e>b:
    print("9")
elif e>b and f>c:
    print("8")
elif d>a and f>c:
    print("7")
elif d>a or e>b or f>c:
    print("6")
else:
    print("5")
