n=int(input())
c=0
s=0
while(n):
    r=n%10
    s+=r*(8**c)
    n=n//10
    c+=1
b=[]
while(s):
    b.append(s%2)
    s=s//2
c=b[::-1]
number=0
for cd in c:
    number= number*10+cd
print(number)