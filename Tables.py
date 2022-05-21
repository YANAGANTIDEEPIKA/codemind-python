N,R=map(int,input().split())
s=1
for R in range(1,R+1):
    if(R%2!=0):
        print(N,'x',R,'=',R*N)
