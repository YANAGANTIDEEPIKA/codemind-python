n=list(map(str,input().split()))
m=0
for i in range(0,len(n)):
    if len(n[i])>m:
        m=len(n[i])
print(m)  