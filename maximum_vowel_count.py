n=input()
z=n.split()
#print(*z)
l=[]
for i in z:
    vowel=sum(letter in 'aeiou'for letter in i.lower())
    l.append(vowel)
print(max(l))