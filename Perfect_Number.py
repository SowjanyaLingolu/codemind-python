num=int(input())
su=0
for i in range(1,num):
    rem=num%i
    if rem==0:
        su=su+i
if su==num:
    print("True")
else:
    print("False")