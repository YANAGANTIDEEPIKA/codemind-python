def length(t):
    c=0
    while(t!=0):
        r=t%10
        t//=10
        c+=1
    return c
N=int(input())
sum=0
t=N
re=0
co=length(t)
while(t!=0):
    r=t%10
    sum=sum+r**co
    t//=10
    co-=1
if(sum==N):
    print('True')
else:
    print('False')