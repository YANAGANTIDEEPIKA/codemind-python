m=int(input())
n=int(input())
sum1=0
for i in range(1,m):
    if(m%i==0):
        sum1+=i
sum2=0
for i in range(1,n):
    if(n%i==0):
        sum2+=i
if(sum2==m and sum1==n):
    print('Amicable')
else:
    print('Not Amicable')