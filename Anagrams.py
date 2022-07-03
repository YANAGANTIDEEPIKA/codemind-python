def anagram(str):
    a=[]
    for c in str.lower():
        a.append(c)
    d={}
    for c in a:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    return d
s1=input()
s2=input()
a=anagram(s1)
b=anagram(s2)
if a==b:
    print("True")
else:
    print("False")