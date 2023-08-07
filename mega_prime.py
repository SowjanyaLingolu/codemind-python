def cd(n):
    while(n):
        di=n%10
        if(di!=2 and di!=3 and di!=5 and di!=7):
            return 0
        n=n//10
    return 1
def prime(n):
    if n==1:
        return 0
    i=2
    while i*i<=n:
        if n%i==0:
            return 0
        i=i+1
    return 1
def full(n):
    return(cd(n) and prime(n))
n=int(input())
if (full(n)):
    print("Mega Prime")
else:
    print("Not Mega Prime")