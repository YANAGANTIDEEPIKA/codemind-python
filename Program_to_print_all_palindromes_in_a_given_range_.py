m=int(input())
n=int(input())
for i in range(m,n+1,1):
    r=0
    t=i
    while t>0:
        re=t%10
        r=(r*10)+re
        t=t//10
    if(r==i):
        print(i,end=' ')