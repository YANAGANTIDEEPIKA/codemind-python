t=int(input())
for i in range(0,t):
    s=input()
    c=0
    for i in range(len(s)):
        if s[i].isdigit():
            c+=1
    if(c>0):
        print("Yes")
    else:
        print("No")