def u(n):
    if n==0:
        return False
    for i in [2,3,5]:
        while n%i==0:
            n/=i
    return n==1
n=int(input())
b=u(n)
if b==True:
    print("Ugly Number")
else:
    print("Not Ugly Number")