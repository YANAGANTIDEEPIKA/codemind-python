N=int(input())
sum=0
for i in range(1,N):
    if(N%i==0):
        sum=sum+i
if(sum>N):
    print('True')
else:
    print('False')
        