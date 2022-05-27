def rev(n):
    re=0
    while(n!=0):
        r=n%10
        re=re*10+r
        n//=10
    return re
n=int(input())
print(rev(n))