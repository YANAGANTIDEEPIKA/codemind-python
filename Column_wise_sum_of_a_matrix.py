n,m=map(int,input().split())
s=[0]*m
for i in range(n):
    m=list(map(int,input().split()))
    for i in range(len(m)):
        s[i]=s[i]+m[i]
for k in s:
    print(k,end=' ')