n=int(input())
s=pow(n,2)
m=pow(10,len(str(n)))
if s%m==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")