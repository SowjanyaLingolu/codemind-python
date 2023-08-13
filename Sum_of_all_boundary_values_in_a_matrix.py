r,c=map(int,input().split())
mat=[]
sum=0
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            sum+=mat[i][j]
print(sum)