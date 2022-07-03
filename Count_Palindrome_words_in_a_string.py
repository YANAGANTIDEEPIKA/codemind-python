def pallin(s):
    if s.lower()==s.lower()[::-1]:
        return True
def copallin(str):
    c=0
    l=str.split(" ")
    #print(l)
    for i in l:
        if (pallin(i)):
            c+=1
    print(c)
s=input()
copallin(s)