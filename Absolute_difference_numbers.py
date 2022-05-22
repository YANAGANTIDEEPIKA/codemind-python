def count(n):
    c=0
    while(n!=0):
        r=n%10
        c+=1
        n//=10
    return c
def first(n,x):
    length=count(n)
    while(length!=x):
        n//=10
        length-=1
    first=n
    return first
def last(n,x):
    i=0
    mod=1
    while(i<x):
        mod=mod*10
        i+=1
    last=n%mod
    return last
N,X=map(int,input().split())
print(abs(last(N,X)-first(N,X)))