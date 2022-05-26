t=int(input())
n=t*t
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n//=10
if(sum==t):
    print('Neon Number')
else:
    print('Not Neon Number')
