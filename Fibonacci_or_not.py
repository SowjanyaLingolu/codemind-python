import math
def per(x):
    s=int(math.sqrt(x))
    return s*s==x
def fibo(n):
    return per(5*n*n+4) or per(5*n*n-4)
num=int(input())
if(fibo(num)==True):
    print("True")
else:
    print("False")