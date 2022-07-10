s=input()
x=s.split(" ")
s=s2=0
for i in x:
    m=ord(min(i))
    s=s+m
    ma=ord(max(i))
    s2=s2+ma
print(s2-s)