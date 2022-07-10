s=list(map(str,input().split()))
c=0
a=len(s)
for i in s:
    c+=1
    if c==a:
        print(i[0])