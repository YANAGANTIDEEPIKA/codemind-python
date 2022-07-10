s=list(map(str,input().split()))
c=0
p='aeiouAEIOU'
for i in s:
    if(i[0] in p) and (i[len(i)-1] not in p):
        c+=1
print(c)