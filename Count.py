n=int(input())
l=list(map(int,input().strip().split()))[:n]
c=0
oc=0
ec=0
for i in range(n):
    if(l[i]%2):
        oc+=1
    else:
        ec+=1
print(ec,oc)