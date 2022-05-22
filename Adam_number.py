def rev(n):
    re=0
    t=n
    while(t!=0):
        r=t%10
        re=re*10+r
        t//=10
    return re
N1=int(input())
s1=N1*N1
N2=rev(N1)
s2=N2*N2
ms=rev(s2)
if(s1==ms):
    print('True')
else:
    print('False')
