r,c=map(int,input().split())
mat=[]
sum=0
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
for i in range(r):
    for j in range(c):
        if j!=0 and j!=c-1 and i!=0 and i!=r-1:
            sum+=mat[i][j]
print(sum)