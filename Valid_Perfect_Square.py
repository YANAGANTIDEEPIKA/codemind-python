t=int(input())
for i in range(1,t+1):
    a=int(input())
    s=0
    for j in range(1,a):
        if(a==j*j):
            s=1
            print('True')
    if(s==0):
        print('False')