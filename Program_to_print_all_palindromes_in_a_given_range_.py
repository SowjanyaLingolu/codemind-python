def pal(n):
    rev=0
    i=n
    while i>0:
        rev=rev*10+i%10
        i//=10
    return n==rev
def cou(minn:int,maxx:int)->None:
    for i in range(minn,maxx+1):
        if pal(i):
            print(i,end=" ")
if __name__=="__main__":
    cou(int(input()),int(input()))
    