m,n=map(int,input().split())
a=m
b=n
for i in range(1,a and b):
    if(a%i==0 and b%i==0):
        gcd=i
lcm=(m*n)/gcd
print("%d"%lcm)