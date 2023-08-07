import math
n=int(input())
o=n
sum=0
while(n):
    r=n%10
    s=math.factorial(r)
    sum+=s
    n=n//10
if sum==o:
    print("The number {} is a strong number".format(o))
else:
    print("The number {} is not a strong number".format(o))