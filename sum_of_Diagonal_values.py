r,c=map(int,input().split())
mat=[]
sum=0
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
for i in range(r):
    for j in range(c):
        if i==j:
            sum+=mat[i][j]
        if (i+j)==r-1 and i!=j:
            sum+=mat[i][j]
print(sum)