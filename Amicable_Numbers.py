a=int(input())
b=int(input())
s1=0
s2=0
for i in range(1,a):
    if a%i==0:
        s1+=i
for j in range(1,b):
    if b%j==0:
        s2+=j
if s1==b and s2==a:
    print("Amicable")
else:
    print("Not Amicable")