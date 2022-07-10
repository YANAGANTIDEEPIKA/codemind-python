t=int(input())
for i in range(1,t+1):
    d=0
    s=input()
    for j in range(len(s)):
        if s[j].isdigit():
            d+=1
    if d==len(s):
        print("True")
    else:
        print("False")