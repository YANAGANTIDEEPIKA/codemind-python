n=int(input())
a=input()
count=0
c=0
for i in a:
    if i=='1':
        c+=1
    if i=='0':
        if c>count:
            count=c
        c=0
if count<c:
    count=c
print(count)