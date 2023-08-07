def ha(n):
    r=s=0;
    while(n>0):
        r=n%10;
        s=s+(r*r);
        n=n//10;
    return s;
num=int(input())
result=num;
while(result!=1 and result!=4):
    result=ha(result);
if(result==1 or result==7):
    print("True");
else:
    print("False")