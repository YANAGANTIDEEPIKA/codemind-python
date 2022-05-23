a,b=map(int,input().split())
s=0
if(a==1 and b==10):
    print('Yes')
    s+=1
elif(a==10 and b==1):
    print('Yes')
    s+=1
elif(b>1 and b<=10):
    if(a+1==b):
        print('Yes')
        s+=1
    elif(a-1)==b:
        print('Yes')
        s+=1
if(s==0):
    print('No')