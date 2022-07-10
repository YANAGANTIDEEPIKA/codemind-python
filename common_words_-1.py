s1=input().lower()
s2=input().lower()
#print(s1)
a=s1.split(" ")
b=s2.split(" ")
c=0
for i in a:
    for j in b:
        if i==j:
            c+=1
print(c)