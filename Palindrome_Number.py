n=int(input())
for i in range(n):
    a=int(input())
    if(str(a)==str(a)[::-1]):
        print("True")
    else:
        print("False")