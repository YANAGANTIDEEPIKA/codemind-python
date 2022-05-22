N=int(input())
t1=0
while(N!=0):
    r=N%10
    if(r>t1):
        l=r
        t1=l
    N//=10
print(l)
    