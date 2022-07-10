s=input()
k=0
v=0
m=0
a=0
i=0
p='aeiouAEIOU'
while(i<len(s)):
    if(s[i] in p):
        k+=1
    elif s[i]>='0' and s[i]<='9':
        v+=1
    elif s[i]==' ':
        m+=1
    else:
        a+=1
    i+=1
print("Vowels: %d"%k)
print("Consonants: %d"%a)
print("Digits: %d"%v)
print("White spaces: %d"%m)


        
        