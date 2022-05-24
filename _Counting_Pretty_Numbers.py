t= int(input())
for i in range(1,t+1):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        p=j%10
        if(p==2 or p==3 or p==9):
            c+=1
    print(c)    
    