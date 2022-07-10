s=input()
x=s.split(" ")
s=s2=0
for i in x:
    m=ord(min(i))
    ma=ord(max(i))
    print(ma-m,end=' ')