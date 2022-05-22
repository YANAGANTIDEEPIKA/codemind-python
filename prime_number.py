N=int(input())
c=0
for i in range(1,N+1):
    if(N%i==0):
        c+=1
if(c==2):
    print('prime')
else:
    print('not a prime')