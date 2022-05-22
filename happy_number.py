def happy(n):
    sum,re=0,0
    while(n!=0):
        r=n%10
        sum=sum+r*r
        n//=10
    return sum
N=int(input())
res=N
while(res>=9):
    res=happy(res)
if(res==1 or res==7):
    print('True')
else:
    print('False')