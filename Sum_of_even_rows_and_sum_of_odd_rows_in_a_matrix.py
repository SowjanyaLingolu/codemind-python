r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
sum1=0
sum2=0
for i in range(r):
    if i%2==0:
        for j in range(c):
            sum1+=mat[i][j]
    else:
        for j in range(c):
            sum2+=mat[i][j]
print(sum1,sum2)
