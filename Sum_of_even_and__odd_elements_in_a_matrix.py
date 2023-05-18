r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
sum1=0
sum2=0
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            sum1+=mat[i][j]
        else:
            sum2+=mat[i][j]
print(sum1,sum2)            
