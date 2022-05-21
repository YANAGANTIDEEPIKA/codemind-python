N=int(input())
t=N
re=0
while t!=0:
    r=t%10
    re=re*10+r
    t//=10
if(N==re):
    print('True')
else:
    print('False')