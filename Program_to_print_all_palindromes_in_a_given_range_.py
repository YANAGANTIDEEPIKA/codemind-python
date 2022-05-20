m=int(input())
n=int(input())
for i in range(m,n+1):
    t=i
    r=0
    while(t>0):
        re=t%10
        r=r*10+re
        t=t//10
    if(i==r):
        print(r,end=' ')