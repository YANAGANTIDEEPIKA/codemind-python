m=int(input())
n=int(input())
for i in range(m,n+1):
    c=0
    x=i
    while(x>0):
        r=x%10
        if(r==0):
            c+=1
            break
        if(i%r!=0):
            c+=1
        x=x//10
    if(c==0):
        print(i,end=' ')