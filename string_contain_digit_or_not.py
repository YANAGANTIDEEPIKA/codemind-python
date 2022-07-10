s=input()
c=0
for i in range(len(s)):
    if s[i].isdigit():
        c+=1
if c>0:
    print('Contains',c,'digit')
else:
    print("Doesn't contain digit")