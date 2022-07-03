s=input().lower()
s1=input().lower()
l=[]
c=0
for i in s:
    if i not in s1:
        l.append(i)
for j in s1:
    if j not in s:
        l.append(j)
for k in sorted(set(l)):
    if k!=' ':
        c+=1
print(c)
        