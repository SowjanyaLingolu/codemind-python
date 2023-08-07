def per(n):
    i=1
    while i*i<=n:
        if i*i==n:
            return True
        i+=1
    return False
num=int(input())
print(per(num))