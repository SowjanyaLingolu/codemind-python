def npd(N):
    c=0
    for i in range(1,N+1):
        if N%i==0:
            if prime(i)==False:
                c+=1
    return c
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
N=int(input())
print(npd(N))