n=input()
c=0
c1=0
p='aeiou'
for i in range(len(n)):
    if n[i] in p:
        c+=1
    else:
        if c1<c:
            c1=c
        c=0
if c1<c:
    c1=c
print(c1)