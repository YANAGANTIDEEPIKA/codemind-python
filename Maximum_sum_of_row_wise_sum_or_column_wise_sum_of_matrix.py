n,m=map(int,input().split())
c=[0]*(m)
b=[]
for i in range(n):
    a=list(map(int,input().split()))
    b.append(sum(a))
    for j in range(m):
        c[j]=c[j]+a[j]
print(max(b+c))
    