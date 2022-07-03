n=int(input())
l=[0]*(n*n)
a=[]
b=[]
for j in range(2):
    for l in range(n):
        m=list(map(int,input().split()))
        if j==0:
            for k in m:
                a.append(k)
        if j==1:
            for h in m:
                b.append(h)
for u in range(n*n):
    if u%n==(n-1):
        print(a[u]+b[u])
    else:
        print(a[u]+b[u],end=' ')
